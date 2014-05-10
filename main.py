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
		logger.info("Requested main page: " + self.request.path)
		page_handler.static_page(self, "index.html")

class PartialsPage(webapp2.RequestHandler):
	def get(self):
		logger.info("Requested partial page: " + self.request.path)
		page_elements = self.request.path.rsplit('/', 1)
		page_handler.static_page(self, "partials/" + page_elements[1])
            
class AdminPage(webapp2.RequestHandler):
	def get(self):
		page_handler.static_page(self, "admin.html", auth_mode = page_handler.AUTH_ADMIN)        
    
application = webapp2.WSGIApplication([
    ('/admin', AdminPage),
    ('/partials/.*', PartialsPage),
    ('/.*', MainPage)
], debug=True)