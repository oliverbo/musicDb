import webapp2
import json
import logging
import musicdb.model
from apptools.data_handler import DataHandler
from musicdb.model import Artist
from musicdb.model import Venue
from musicdb import tools

logger = logging.getLogger("resource")

# access levels
ACCESS_NONE = 0
ACCESS_ALL = 1
ACCESS_ADMIN = 2

_resource_map = {
	'/api/venue' : {'handler' : DataHandler.get_handler('venue'), 'get' : ACCESS_ALL, 'post' : ACCESS_ADMIN} ,
	'/api/artist' : {'handler' : DataHandler.get_handler('artist'), 'get' : ACCESS_ALL, 'post' : ACCESS_ADMIN}
}

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
			data_handler = resource_descriptor['handler']
			
			if not key:
				result = data_handler.query()
			else:
				result = data_handler.find(key)
				if not result:
					self.response.status = '404 Not Found'
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
			data_handler = resource_descriptor['handler']
			data = json.loads(self.request.body)
			logger.debug("Data: %s", data)
			data_handler.save(data)

application = webapp2.WSGIApplication([
    ('/api/.*', ResourceHandler)
], debug=True)