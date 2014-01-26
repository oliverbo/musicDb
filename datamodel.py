import webapp2
import json
from musicdb.model import Artist
from musicdb import tools


class Test(webapp2.RequestHandler):
    
    def get(self):
        artist = Artist()
        artist.canonicalName = "@emikatwit"
        artist.displayName = "Emika"
        
        artists = [artist]
        
        artist = Artist()
        artist.canonicalName = "@laurelhalo"
        artist.displayName = "Laurel Halo"
        artists.append(artist)
        
        r = tools.ndb_to_json(artists)
        self.response.content_type = "application/json"
        self.response.write(r)

application = webapp2.WSGIApplication([
    ('/api/artist', Test)
], debug=True)