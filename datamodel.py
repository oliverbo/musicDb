import webapp2
import json
import logging
from musicdb.model import Artist
from musicdb import tools

logger = logging.getLogger("datamodel")


class ArtistHandler(webapp2.RequestHandler):
    
    def get(self):
        artist = Artist()
        artist.canonicalName = "@emikatwit"
        artist.displayName = "Emika"
        
        artists = [artist]
        
        artist = Artist()
        artist.canonicalName = "@laurelhalo"
        artist.displayName = "Laurel Halo"
        artists.append(artist)
        
        artist = Artist()
        artist.canonicalName = "@gazelletwin"
        artist.displayName = "Gazelle Twin"
        artists.append(artist)
        
        r = tools.ndb_to_json(artists)
        self.response.content_type = "application/json"
        self.response.write(r)
        
    def post(self):
        logger.info("received post request: %s ", self.request.body);
        artist = json.loads(self.request.body);
        logger.info("--- %s", artist);

application = webapp2.WSGIApplication([
    ('/api/artist', ArtistHandler)
], debug=True)