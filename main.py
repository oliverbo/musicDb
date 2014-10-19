import os
import urllib
import logging
import eapptools
import json

from google.appengine.api import users
from musicdb import tools
from musicdb.music_model import Venue

import webapp2
import jinja2

logger = logging.getLogger("main")


class ExportPage(webapp2.RequestHandler):
	def get(self):
		logger.info("Export requested")
		if users.is_current_user_admin():
			self.response.content_type = 'text/plain'
			data = Venue.export_as_json()
			self.response.write(data)
		else:
			logger.warn("Unauthorized export request")
			self.response.status = "403 Forbidden"
			
class ImportPage(webapp2.RequestHandler):
	def post(self):
		if users.is_current_user_admin():
			logger.info("Importing data file...")
			json_data = self.request.get('uploadFile')
			logger.debug(json_data)
			
			# delete all existing venues
			Venue.delete_all()
			
			# import data into venue db
			Venue.import_from_json(json_data)
			
			# Write to screen
			self.response.write('<html><body>Import successful</body></html>')
		else:
			logger.warn("Unauthorized import request")
			self.response.status = "403 Forbidden"
		    
application = webapp2.WSGIApplication([
    ('/x/export', ExportPage),
    ('/x/import', ImportPage),
], debug=True)