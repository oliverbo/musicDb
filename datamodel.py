import webapp2
import json
import logging
import musicdb.model
from musicdb.model import Artist
from musicdb.model import Venue
from musicdb import tools

logger = logging.getLogger("datamodel")


class ArtistHandler(webapp2.RequestHandler):
    
    def get(self):
        artist_query = Artist.query(ancestor=musicdb.model.artist_parent_key())
        artists = artist_query.fetch(10)        
        r = tools.ndb_to_json(artists)
        self.response.content_type = "application/json"
        self.response.write(r)
        
    def post(self):
        logger.info("received post request: %s ", self.request.body)
        artist_data = json.loads(self.request.body)
        logger.info("--- %s", artist_data)
        artist = Artist(parent = musicdb.model.artist_parent_key())
        artist.copy_data(artist_data)
        artist.put()
        
class VenueHandler(webapp2.RequestHandler):
    def get(self):
        venues_query = Venue.query(ancestor=musicdb.model.venue_parent_key())
        venues = venues_query.fetch(10)        
        r = tools.ndb_to_json(venues)
        self.response.content_type = "application/json"
        self.response.write(r)
        
    def post(self):
        logger.info("received post request: %s ", self.request.body)
        venue_data = json.loads(self.request.body)
        logger.info("--- %s", venue_data)
        venue = Venue(parent = musicdb.model.venue_parent_key())
        venue.copy_data(venue_data)
        venue.put()

application = webapp2.WSGIApplication([
    ('/api/artist', ArtistHandler),
    ('/api/venue', VenueHandler)
], debug=True)