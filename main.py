import os
import urllib
import logging

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.redirect('html/index.html', True)
        
class AdminPage(webapp2.RequestHandler):
    def get(self):
        self.redirect('html/admin.html', True)
    

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/admin', AdminPage)
], debug=True)