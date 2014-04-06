import os
import urllib
import logging

from google.appengine.api import users

import webapp2
import jinja2

logger = logging.getLogger("main")
JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + '/html'),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.redirect('html/index.html', True)
        
class AdminPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
                
        if (user):
            logger.info('Authenticated user: %s', user.nickname())
            template = JINJA_ENVIRONMENT.get_template('admin.html')
            template_values = { "userName" : user.nickname()}
            self.response.write(template.render(template_values))
        else:
            logger.info('No user authenticated')
            self.redirect(users.create_login_url('/admin2'))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/admin2', AdminPage)
], debug=True)