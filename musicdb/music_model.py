# Music model classes

import logging
import json
import re
import string
from google.appengine.ext import ndb
from eapptools.model import ModelBase
import eapptools.validation as val

INVALID_CHARS = re.compile('[ .,:/]')

logger = logging.getLogger("music_data_handler")
                    
class Venue(ModelBase):
	model_name = "VENUE"
	displayName = ndb.StringProperty()
	address = ndb.StringProperty()
	zipCode = ndb.StringProperty()
	city = ndb.StringProperty()
	state = ndb.StringProperty()
	neighborhood = ndb.StringProperty()
	website = ndb.StringProperty()
	twitterName = ndb.StringProperty()
	facebookURI = ndb.StringProperty()
	phoneNumber = ndb.StringProperty()
	priceLevel = ndb.IntegerProperty()
	specialTip = ndb.StringProperty()
	description = ndb.StringProperty()
	capacity = ndb.IntegerProperty()
	booking = ndb.StringProperty()
	publicTransportation = ndb.StringProperty()
	
	@classmethod
	def parent_key(cls):
		return ndb.Key('Base', 'venue')
        
	@classmethod
	def create(cls, data_dict):
		result = []
		venue = Venue(parent = cls.parent_key())
		
		logger.info("Copying data into venue %s", venue.key)
		
		if (data_dict):				
			venue.uniqueName = val.get_string(data_dict, 'uniqueName', result, mandatory = True)
			#venue.uniqueName = INVALID_CHARS.sub('', venue.uniqueName)
			venue.displayName = val.get_string(data_dict, 'displayName', result, mandatory = True)
			venue.address = val.get_string(data_dict, 'address', result)
			venue.zipCode = val.get_string(data_dict, 'zipCode', result)
			venue.city = val.get_string(data_dict, 'city', result)
			venue.state	= val.get_string(data_dict, 'state', result)
			venue.neighborhood = val.get_string(data_dict, 'neighborhood', result)
			venue.twitterName = val.get_string(data_dict, 'twitterName', result)		
			venue.facebookURI = val.get_string(data_dict, 'facebookURI', result)
			venue.phoneNumber = val.get_string(data_dict, 'phoneNumber', result)
			venue.priceLevel = val.get_int(data_dict, 'priceLevel', result)
			venue.description = val.get_string(data_dict, 'description', result)
			venue.capacity = val.get_int(data_dict, 'capacity', result)
			venue.booking = val.get_string(data_dict, 'booking', result)
			venue.specialTip = val.get_string(data_dict, 'specialTip', result)
			venue.publicTransportation = val.get_string(data_dict, 'publicTransportation', result)
		else:			
			result.append(val.ValidationResult(ERR_DATA_MISSING, error_message="Empty record" ))
			
		logger.debug("Populated venue: %s", venue)	
			
		if len(result) > 0:
			if logger.getEffectiveLevel() == logging.DEBUG:
				for r in result:
					logger.debug("Error '%s' (%d) in %s", r.errorMessage, r.errorCode, r.field)
			raise val.ValidationError(result)
		else:
			return venue