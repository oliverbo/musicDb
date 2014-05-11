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
	def get(self):
		logger.info('API request %s', self.request.path)
		page_elements = self.request.path.rsplit('/', 1)
		data_handler_name = _path_map[page_elements[1]]
		if not data_handler_name:
			request_handler.response.status = '404 Not Found'
		else:
			logger.info("Requested data handler %s", data_handler_name)
			data_handler = DataHandler.get_handler(_path_map[data_handler_name])
			result = data_handler.query()
			r = tools.ndb_to_json(result)
			self.response.content_type = "application/json"
			self.response.write(r)
	
	def post(self):
		logger.info("received post request: %s ", self.request.body)
		artist_data = json.loads(self.request.body)
		logger.info("--- %s", artist_data)
		artist = Artist(parent = musicdb.model.artist_parent_key())
		artist.copy_data(artist_data)
		artist.put()

application = webapp2.WSGIApplication([
    ('/api/.*', ResourceHandler)
], debug=True)