# Main file for application objects and configuration

import webapp2
import eapptools
from eapptools.resource import ResourceHandler
from eapptools.resource import ResourceDescriptor
from music_model import Venue

resource_config = {
	'mapping' : {
		 '/api/venue' : ResourceDescriptor(Venue, eapptools.ACCESS_ALL, eapptools.ACCESS_ADMIN, eapptools.ACCESS_ADMIN)
	}
}

resource_handler = webapp2.WSGIApplication([
    ('/api/.*', ResourceHandler)
], debug=True, config = resource_config)