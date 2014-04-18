import os
import urllib
import logging

from google.appengine.api import users

import jinja2

AUTH_NONE = 0
AUTH_USER = 1
AUTH_ADMIN = 2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + '/../html'),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

logger = logging.getLogger("page_handler")
logger.info("Root Dir %s", os.path.dirname(__file__) + '/../html')
    
def static_page(request_handler, page_name, page_dir = 'html', auth_mode = AUTH_NONE):
    user = users.get_current_user()
                
    if user or auth_mode == AUTH_NONE:
        logger.info("User %s is not an admin!", user.nickname())
        if not users.is_current_user_admin() and auth_mode == AUTH_ADMIN:
            request_handler.response.status = '401 Not Authorized'
            
        logger.info('Authenticated user: %s', user.nickname())
        template = JINJA_ENVIRONMENT.get_template(page_name)
        template_values = { "userName" : user.nickname()}
        request_handler.response.write(template.render(template_values))
    else:
        logger.info('No user authenticated')
        request_handler.redirect(users.create_login_url('/admin'))