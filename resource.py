import webapp2
import json
import logging
import musicdb.model
from apptools.data_handler import DataHandler
from google.appengine.api import users
from musicdb.music_data_handler import VenueHandler
from musicdb.music_data_handler import ArtistHandler
from musicdb import tools

logger = logging.getLogger("resource")

# access levels
ACCESS_NONE = 0
ACCESS_ALL = 1
ACCESS_ADMIN = 2

_resource_map = {
	'/api/venue' : {'handler' : VenueHandler(), 'get' : ACCESS_ALL, 'post' : ACCESS_ADMIN, 'delete' : ACCESS_ADMIN} ,
	'/api/artist' : {'handler' : ArtistHandler(), 'get' : ACCESS_ALL, 'post' : ACCESS_ADMIN, 'delete' : ACCESS_ADMIN}
}

ERR_VALIDATION = 1000

ERROR_CODES = {
	ERR_VALIDATION : "Validation Error"
}

class ErrorResponse:
	errorCode = 0 
	errorMessage = None
	details = None
	
	def __init__(self, error_code, details = None, error_message = None):
		self.errorCode = error_code
		if details:
			self.details = details
		if error_message:
			self.errorMessage = error_message
		elif error_code in ERROR_CODES:
			self.errorMessage = ERROR_CODES[error_code]
			
	def to_json(self):
		return tools.to_json(self)

class ResourceHandler(webapp2.RequestHandler):

	def _get_resource_descriptor(self, path):
		path_elements = self.request.path.split('/')
		
		# Looping through the elements to find a matching handler
		resource_path = ''
		key = None
		resource_descriptor = None
		for p in path_elements:
			logger.debug("Element %s", p)		
			if not resource_descriptor:
				resource_path += p
				logger.debug('looking for resource descriptor for %s', resource_path)
				if resource_path in _resource_map:
					logger.debug("resource descriptor found for %s", resource_path)
					resource_descriptor = _resource_map[resource_path]
					key = ''
				else:
					resource_path += '/'
			elif key == '':
				key += p
				logger.debug('key %s', key)
			else:
				key += '/' + p
		
		if resource_descriptor:
			logger.info("Resource descriptor found for %s and key '%s'", resource_path, key)
			return (resource_descriptor, key)
		else:
			return (None, None)

	def get(self):
		logger.info('API request %s', self.request.path)
		(resource_descriptor, key) = self._get_resource_descriptor(self.request.path)
		
		if not resource_descriptor:
			self.response.status = '400 Bad Request'
		else:
			permission = resource_descriptor['get']
			if permission == ACCESS_NONE or (permission == ACCESS_ADMIN and not users.is_current_user_admin()):
				self.response.status = '403 Not Authorized'
			else:
				data_handler = resource_descriptor['handler']
			
				if not key:
					result = data_handler.query()
					logger.debug('Result: %s', result)
				else:
					result = data_handler.find(key)
				if not result:
					self.response.status = '404 Not Found'
				else:
					r = tools.ndb_to_json(result)
					logger.debug(r)
					self.response.content_type = "application/json"
					self.response.write(r)
	
	def post(self):
		logger.info("received post request: %s ", self.request.body)
		(resource_descriptor, key) = self._get_resource_descriptor(self.request.path)
		if not resource_descriptor:
			self.response.status = '400 Bad Request'
		else:
			permission = resource_descriptor['post']
			if permission == ACCESS_NONE or (permission == ACCESS_ADMIN and not users.is_current_user_admin()):
				self.response.status = '403 Not Authorized'
			else:
				data_handler = resource_descriptor['handler']
				data = json.loads(self.request.body)
				logger.debug("Data: %s", data)
				try:
					data_handler.save(data, key)
				except musicdb.model.ValidationError as e:
					self.response.status = '400 Bad Request'
					self.response.content_type = "application/json"
					response_message = ErrorResponse(ERR_VALIDATION, e.result).to_json()
					logger.debug("Error message: %s", response_message)
					self.response.write(response_message)
			
	def delete(self):
		logger.info("received delete request: %s ", self.request.body)
		(resource_descriptor, key) = self._get_resource_descriptor(self.request.path)
		if not resource_descriptor or not key:
			self.response.status = '400 Bad Request'
		else:
			permission = resource_descriptor['delete']
			if permission == ACCESS_NONE or (permission == ACCESS_ADMIN and not users.is_current_user_admin()):
				self.response.status = '403 Not Authorized'
			else:
				data_handler = resource_descriptor['handler']
				data_handler.delete(key)

application = webapp2.WSGIApplication([
    ('/api/.*', ResourceHandler)
], debug=True)