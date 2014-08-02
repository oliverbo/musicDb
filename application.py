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
	'/api/venue' : ResourceDescriptor(Venue, eapptools.ACCESS_ALL, eapptools.ACCESS_ADMIN, eapptools.ACCESS_ADMIN)
}

# page mapping
config[eapptools.CFG_PAGE_MAPPING] = {
	'/index.html' : PageDescriptor(),
	'/partials/venues.html' : PageDescriptor(),
	'/partials/venuePage.html' : PageDescriptor(),
	'/partials/venuePageAdmin.html' : PageDescriptor(access=eapptools.ACCESS_ADMIN)
}

resource_handler = webapp2.WSGIApplication([
    ('/api/.*', ResourceHandler)
], debug=True, config = config)


page_handler = webapp2.WSGIApplication([
	('/.*', PageHandler)
], debug=True, config = config)