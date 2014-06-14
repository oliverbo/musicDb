# Model classes

import json
from google.appengine.ext import ndb

ERR_INVALID_NUMBER = 1000
ERR_DATA_MISSING = 1001

VALIDATION_ERRORS = {
	ERR_INVALID_NUMBER : "Invalid Number",
	ERR_DATA_MISSING : "Mandatory field missing"
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
	
	def validate(self):
		pass

	def copy_data_and_validate(self, data_dict):
		pass
                
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
        
	def copy_data_and_validate(self, data_dict):
		result = []
		
		if (data_dict):		
			if ('uniqueName' in data_dict):
				self.uniqueName = data_dict['uniqueName']
			else:
				result.append(ValidationResult(ERR_DATA_MISSING, "uniqueName"))
				
			if ('displayName' in data_dict):
				self.displayName = data_dict['displayName']
			else:
				result.append(ValidationResult(ERR_DATA_MISSING, "displayName"))
			
			if ('address' in data_dict):				
				self.address = data_dict['address']
				
			if ("zipCode" in data_dict):
				self.zipCode = data_dict['zipCode']
				
			if ("city" in data_dict):
				self.city = data_dict['city']
				
			if ("state" in data_dict):	
				self.state = data_dict['state']
			
			if ("neighborhood" in data_dict):		
				self.neighborhood = data_dict['neighborhood']
				
			if ("website" in data_dict):
				self.website = data_dict['website']
				
			if ("twitterName" in data_dict):
				self.twitterName = data_dict['twitterName']
				
			if ("facebookURI" in data_dict):
				self.facebookURI = data_dict['facebookURI']
	
			if ("phoneNumber" in data_dict):
				self.phoneNumber = data_dict['phoneNumber']
			
			if ("priceLevel" in data_dict):
				try:
					self.priceLevel = int(data_dict['priceLevel'])
				except:
					result.append(ValidationResult(ERR_INVALID_NUMBER, 'priceLevel'))
				
			if ("description" in data_dict):
				self.description = data_dict['description']
			
			try:            
				self.capacity = int(data_dict['capacity'])
			except ValueError:
				result.append(ValidationResult(ERR_INVALID_NUMBER, 'capacity'))

			if ("booking" in data_dict):
				self.booking = data_dict['booking']
				
			if ("specialTip" in data_dict):	
				self.specialTip = data_dict['specialTip']
		else:
			result.append(ValidationResult(ERR_DATA_MISSING, error_message="Empty record" ))
			
		if len(result) > 0:
			raise ValidationError(result)