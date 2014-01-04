import os
import urllib
import logging

import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.redirect('html/index.html', True)        

application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)