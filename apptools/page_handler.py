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
    
    logger.info("auth_mode: %d", auth_mode)
    if user:
    	logger.info('authenticated user: %s', user.nickname())
    	logger.info('user is admin: %s', users.is_current_user_admin())
    else:
    	logger.info('no authenticated user')
                
    if user or auth_mode == AUTH_NONE:
        if not users.is_current_user_admin() and auth_mode == AUTH_ADMIN:
			request_handler.response.status = '401 Not Authorized'
			return
        template = JINJA_ENVIRONMENT.get_template(page_name)
        
        template_values = {
        	'logoutURI' : users.create_logout_url('/')
        	}
        if user:
        	template_values["userName"] = user.nickname()
        	
        request_handler.response.write(template.render(template_values))
    else:
        logger.info('No user authenticated')
        request_handler.redirect(users.create_login_url('/admin'))