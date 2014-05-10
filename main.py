import os
import urllib
import logging
import apptools

from google.appengine.api import users
from apptools import page_handler

import webapp2
import jinja2

logger = logging.getLogger("main")
apptools.web_root = os.path.dirname(__file__) + '/html'

class MainPage(webapp2.RequestHandler):
	def get(self):
		page_handler.static_page(self, "index.html")

class ArtistsPage(webapp2.RequestHandler):
	def get(self):
		page_handler.static_page(self, "partials/artists.html")

            
class AdminPage(webapp2.RequestHandler):
	def get(self):
		page_handler.static_page(self, "admin.html", auth_mode = page_handler.AUTH_ADMIN)        
    
application = webapp2.WSGIApplication([
    ('/admin', AdminPage),
    ('/html/partials/artists.html', ArtistsPage),
    ('/.*', MainPage)
], debug=True)