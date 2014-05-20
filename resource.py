import webapp2
import json
import logging
import musicdb.model
from apptools.data_handler import DataHandler
from musicdb.model import Artist
from musicdb.model import Venue
from musicdb import tools

logger = logging.getLogger("resource")

_path_map = {
	'venue' : 'venue',
	'artist' : 'artist'
}

class ResourceHandler(webapp2.RequestHandler):

	def _get_data_handler(self, path):
		page_elements = self.request.path.rsplit('/', 1)
		data_handler_name = _path_map[page_elements[1]]
		logger.info("Requested data handler %s", data_handler_name)
		
		if not data_handler_name:
			return None
		else:
			logger.info("Requested data handler %s", data_handler_name)
			return DataHandler.get_handler(_path_map[data_handler_name])

	def get(self):
		logger.info('API request %s', self.request.path)
		data_handler = self._get_data_handler(self.request.path)
		
		if not data_handler:
			request_handler.response.status = '404 Not Found'
		else:
			result = data_handler.query()
			r = tools.ndb_to_json(result)
			self.response.content_type = "application/json"
			self.response.write(r)
	
	def post(self):
		logger.info("received post request: %s ", self.request.body)
		data_handler = self._get_data_handler(self.request.path)
		if not data_handler:
			request_handler.response.status = '404 Not Found'
		else:
			data = json.loads(self.request.body)
			logger.debug("Data: %s", data)
			data_handler.save(data)

application = webapp2.WSGIApplication([
    ('/api/.*', ResourceHandler)
], debug=True)