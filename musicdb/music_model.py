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
        
	def copy_from_dict(self, data_dict):
		result = []
		logger.debug("Copying data into venue %s", self.key)
		
		if (data_dict):				
			self.uniqueName = val.get_string(data_dict, 'uniqueName', result, mandatory = True)
			self.uniqueName = INVALID_CHARS.sub('', self.uniqueName)
			self.displayName = val.get_string(data_dict, 'displayName', result, mandatory = True)
			self.address = val.get_string(data_dict, 'address', result)
			self.zipCode = val.get_string(data_dict, 'zipCode', result)
			self.city = val.get_string(data_dict, 'city', result)
			self.state	= val.get_string(data_dict, 'state', result)
			self.neighborhood = val.get_string(data_dict, 'neighborhood', result)
			self.twitterName = val.get_string(data_dict, 'twitterName', result)		
			self.facebookURI = val.get_string(data_dict, 'facebookURI', result)
			self.phoneNumber = val.get_string(data_dict, 'phoneNumber', result)
			self.priceLevel = val.get_int(data_dict, 'priceLevel', result)
			self.description = val.get_string(data_dict, 'description', result)
			self.capacity = val.get_int(data_dict, 'capacity', result)
			self.booking = val.get_string(data_dict, 'booking', result)
			self.specialTip = val.get_string(data_dict, 'specialTip', result)
			self.publicTransportation = val.get_string(data_dict, 'publicTransportation', result)
		else:			
			result.append(val.ValidationResult(ERR_DATA_MISSING, error_message="Empty record" ))
			
		logger.debug("Populated venue: %s", self)	
			
		if len(result) > 0:
			if logger.getEffectiveLevel() == logging.DEBUG:
				for r in result:
					logger.debug("Error '%s' (%d) in %s", r.errorMessage, r.errorCode, r.field)
			raise val.ValidationError(result)