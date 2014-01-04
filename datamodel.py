import webapp2
import json
from musicdb.model import Artist
from musicdb import tools


class Test(webapp2.RequestHandler):
    
    def get(self):
        artist = Artist()
        artist.canonical_name = "@emikatwit"
        artist.display_name = "Emika"
        
        artists = [artist]
        
        r = tools.to_json(artists)
        self.response.content_type = "application/json"
        self.response.write(r)

application = webapp2.WSGIApplication([
    ('/api/artist', Test)
], debug=True)