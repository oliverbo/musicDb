# Model classes

import logging
import json
import re
import string
from google.appengine.ext import ndb
from eapptools.model_base import ModelBase

logger = logging.getLogger("music_data_handler")

ERR_INVALID_NUMBER = 1000
ERR_DATA_MISSING = 1001
ERR_DUPLICATE_KEY = 1002

VALIDATION_ERRORS = {
	ERR_INVALID_NUMBER : "Invalid Number",
	ERR_DATA_MISSING : "Mandatory field missing",
	ERR_DUPLICATE_KEY : "Duplicate Key"
}

INVALID_CHARS = re.compile('[ .,:/]')

class ValidationError(Exception):
	result = None

	def __init__(self, result):
		self.result = result

class ValidationResult:
	errorCode = 0;
	errorMessage = None;
	field = None;
	
	def __init__(self, error_code, field = None, error_message = None):
		self.errorCode = error_code;
		self.field = field
		if error_message:		
			self.errorMessage = error_message
		elif error_code in VALIDATION_ERRORS:
			self.errorMessage = VALIDATION_ERRORS[error_code]
                    
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
			if ('uniqueName' in data_dict):
				venue.uniqueName = string.lower(data_dict['uniqueName'])
				venue.uniqueName = INVALID_CHARS.sub('', venue.uniqueName)
				logger.debug("Saving venue '%s'", venue.uniqueName)
			else:
				result.append(ValidationResult(ERR_DATA_MISSING, "uniqueName"))
				
			# check uniqueness of the key - doesn't work right now
			# venues_query = Venue.query(Venue.uniqueName == self.uniqueName)
			# venues = venues_query.fetch(1)
			# if len(venues) > 0:
			#	logger.debug("Found venue %s with uniqueName %s", venues[0].key, venues[0].uniqueName)
			# if len(venues) <> 0 and venues[0].key != self.key:
			#	result.append(ValidationResult(ERR_DUPLICATE_KEY, "uniqueName"))
				
			if 'displayName' in data_dict:
				venue.displayName = data_dict['displayName']
			else:
				result.append(ValidationResult(ERR_DATA_MISSING, "displayName"))
			
			if 'address' in data_dict:				
				venue.address = data_dict['address']
				
			if "zipCode" in data_dict:
				venue.zipCode = data_dict['zipCode']
				
			if "city" in data_dict:
				venue.city = data_dict['city']
				
			if "state" in data_dict:	
				venue.state = data_dict['state']
			
			if "neighborhood" in data_dict:		
				venue.neighborhood = data_dict['neighborhood']
				
			if "website" in data_dict:
				venue.website = data_dict['website']
				
			if "twitterName" in data_dict:
				venue.twitterName = data_dict['twitterName']
				
			if "facebookURI" in data_dict:
				venue.facebookURI = data_dict['facebookURI']
	
			if "phoneNumber" in data_dict:
				venue.phoneNumber = data_dict['phoneNumber']
			
			if "priceLevel" in data_dict and data_dict['priceLevel']:
				try:
					venue.priceLevel = int(data_dict['priceLevel'])
				except:
					result.append(ValidationResult(ERR_INVALID_NUMBER, 'priceLevel'))
				
			if "description" in data_dict:
				venue.description = data_dict['description']
			
			if "capacity" in data_dict:
				try:
					venue.capacity = int(data_dict['capacity'])
				except ValueError:
					result.append(ValidationResult(ERR_INVALID_NUMBER, 'capacity'))

			if "booking" in data_dict:
				venue.booking = data_dict['booking']
				
			if "specialTip" in data_dict:	
				venue.specialTip = data_dict['specialTip']
				
			if "publicTransportation" in data_dict:
				logger.debug('-- %s', data_dict['publicTransportation'])
				venue.publicTransportation = data_dict['publicTransportation']
		else:			
			result.append(ValidationResult(ERR_DATA_MISSING, error_message="Empty record" ))
			
		if len(result) > 0:
			if logger.getEffectiveLevel() == logging.DEBUG:
				for r in result:
					logger.debug("Error '%s' (%d) in %s", r.errorMessage, r.errorCode, r.field)
			raise ValidationError(result)
		else:
			return venue