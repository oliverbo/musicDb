# Main file for application objects and configuration

import os
import logging
import webapp2
import eapptools
from eapptools.resource import ResourceHandler
from eapptools.resource import ResourceDescriptor
from eapptools.page import PageHandler
from eapptools.page import PageDescriptor
from musicdb.music_model import Venue

logger = logging.getLogger("application")

# get default config settings
config = eapptools.get_config()

# set application root
config[eapptools.CFG_GLOBAL_APP_DIR] = os.path.dirname(__file__)

# resource mapping
config[eapptools.CFG_RESOURCE_MAPPING] = {
	'/api/venue' : ResourceDescriptor(Venue, eapptools.ACCESS_ALL, eapptools.ACCESS_ADMIN, eapptools.ACCESS_ADMIN,
		auto_create = True)
}

# page mapping
config[eapptools.CFG_PAGE_MAPPING] = {
	'/index.html' : PageDescriptor(),
	'/partials/venues.html' : PageDescriptor(),
	'/partials/venuePage.html' : PageDescriptor(),
	'/partials/venuePageAdmin.html' : PageDescriptor(access=eapptools.ACCESS_ADMIN)
}

# production JavaScripts
config[eapptools.CFG_PROD_JS] = [
	"https://ajax.googleapis.com/ajax/libs/angularjs/1.2.23/angular.min.js",
	"https://ajax.googleapis.com/ajax/libs/angularjs/1.2.23/angular-route.min.js",
	"https://ajax.googleapis.com/ajax/libs/angularjs/1.2.23/angular-resource.min.js",
	"/js/ui-bootstrap-tpls-0.10.0.js"
]

# development JavaScripts
config[eapptools.CFG_DEV_JS] = [
	"/jslib/angular/angular.js",
	"/jslib/angular-route/angular-route.js",
	"/jslib/angular-resource/angular-resource.js",
	"/jslib/angular-bootstrap/ui-bootstrap.js"
]

resource_handler = webapp2.WSGIApplication([
    ('/api/.*', ResourceHandler)
], debug=True, config = config)


page_handler = webapp2.WSGIApplication([
	('/.*', PageHandler)
], debug=True, config = config)