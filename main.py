import os
import urllib
import logging
import apptools

from google.appengine.api import users
from apptools import page_handler

import webapp2
import jinja2

logger = logging.getLogger("main")
apptools.root = os.path.dirname(__file__)

class MainPage(webapp2.RequestHandler):
	def get(self):
		page_handler.static_page(self, "index.html")
            
class AdminPage(webapp2.RequestHandler):
	def get(self):
		page_handler.static_page(self, "admin.html", auth_mode = page_handler.AUTH_ADMIN)        
    
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/admin', AdminPage)
], debug=True)