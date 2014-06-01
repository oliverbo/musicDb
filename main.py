import os
import urllib
import logging
import apptools
import json

from google.appengine.api import users
from musicdb import tools
from musicdb.model import Venue
from apptools import page_handler
from musicdb.music_data_handler import VenueHandler

import webapp2
import jinja2

logger = logging.getLogger("main")
apptools.web_root = os.path.dirname(__file__) + '/html'

ACCESS_ALL = 1
ACCESS_ADMIN = 2

page_info = {
	'venues.html' : {'file' : 'partials/venues.html', 'access' : ACCESS_ALL},
	'venuePage.html' : {'file' : 'partials/venuePage.html', 'access' : ACCESS_ALL},
	'venuePageAdmin.html' : {'file' : 'partials/venuePageAdmin.html', 'access' : ACCESS_ADMIN}
}

class MainPage(webapp2.RequestHandler):
	def get(self):
		logger.info("Requested main page: " + self.request.path)
		page_handler.static_page(self, "index.html")

class PartialsPage(webapp2.RequestHandler):
	def get(self):
		logger.info("Requested partial page: " + self.request.path)
		page_elements = self.request.path.rsplit('/', 1)
		if page_elements[1] in page_info:
			page_descriptor = page_info[page_elements[1]]
			if page_descriptor["access"] == ACCESS_ADMIN and not users.is_current_user_admin():
				self.response.status = '403 Not Authorized'	
			else:	
				page_handler.static_page(self, page_descriptor['file'])
		else:
			self.response.status = '404 not found'

class ExportPage(webapp2.RequestHandler):
	def get(self):
		logger.info("Export requested")
		if users.is_current_user_admin():
			# This is done this way until a central handler repository is implemented
			venue_handler = VenueHandler()
			venues = venue_handler.export_data()
			self.response.content_type = 'text/plain'
			self.response.write(tools.ndb_to_json(venues))
		else:
			logger.warn("Unauthorized export request")
			self.response.status = "403 Forbidden"
			
class ImportPage(webapp2.RequestHandler):
	def post(self):
		if users.is_current_user_admin():
			logger.info("Importing data file...")
			json_data = self.request.get('uploadFile')
			logger.debug(json_data)
			venue_handler = VenueHandler()
			# delete all existing venues
			venue_handler.delete_all()
			
			# convert data to venues
			data = json.loads(json_data)
			venues = []
			for v in data:
				logger.debug("--- %s", v)
				venues.append(v)
			
			# import new data
			venue_handler.import_data(venues)
			self.response.write('<html><body>Import successful</body></html>')
		else:
			logger.warn("Unauthorized import request")
			self.response.status = "403 Forbidden"
		    
application = webapp2.WSGIApplication([
    ('/partials/.*', PartialsPage),
    ('/export', ExportPage),
    ('/import', ImportPage),
    ('/.*', MainPage)
], debug=True)