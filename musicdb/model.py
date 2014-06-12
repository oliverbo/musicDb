# Model classes

import json
from google.appengine.ext import ndb

ERR_INVALID_NUMBER = 1000

VALIDATION_ERRORS = {
	ERR_INVALID_NUMBER : "Invalid Number"
}

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
			

class ModelBase(ndb.Model):
	model_name = "BASE"
	uniqueName = ndb.StringProperty()
	displayName = ndb.StringProperty()
	
	def validate(self, data):
		pass

	def copy_data(self, data_dict):
		pass
		
def artist_parent_key():
	return ndb.Key('Base', 'artist')
    
# An artist model
class Artist(ModelBase):
	model_name = 'ARTIST'
	startYear = ndb.StringProperty()

	def copy_data(self, artist_data):
		if (artist_data):
			self.uniqueName = artist_data['uniqueName']
			self.displayName = artist_data['displayName']
			self.startYear = artist_data['startYear']
            
def venue_parent_key():
	return ndb.Key('Base', 'venue')
    
class Venue(ModelBase):
	model_name = "VENUE"
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
        
	def copy_data(self, data_dict):
		result = []
		
		if (data_dict):
			self.uniqueName = data_dict['uniqueName']
			self.displayName = data_dict['displayName']
			self.address = data_dict['address']
			self.zipCode = data_dict['zipCode']
			self.city = data_dict['city']
			self.state = data_dict['state']
			self.neighborhood = data_dict['neighborhood']
			self.website = data_dict['website']
			self.twitterName = data_dict['twitterName']
			self.facebookURI = data_dict['facebookURI']
			self.phoneNumber = data_dict['phoneNumber']
			self.priceLevel = int(data_dict['priceLevel'])
			self.description = data_dict['description']
			
			try:            
				self.capacity = int(data_dict['capacity'])
			except ValueError:
				result.append(ValidationResult(ERR_INVALID_NUMBER, 'capacity'))

			self.booking = data_dict['booking']
			self.specialTip = data_dict['specialTip']
			
			if len(result) > 0:
				raise ValidationError(result)
		
	def validate(self, data):
		return true