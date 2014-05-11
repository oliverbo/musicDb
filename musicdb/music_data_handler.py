# Data Handlers for Music DB

from apptools.data_handler import DataHandler
import musicdb
from musicdb.model import Artist
from musicdb.model import Venue

# Handler for Artists

class VenueHandler(DataHandler):
	def query(self):
		venues_query = Venue.query(ancestor=musicdb.model.venue_parent_key())
		return venues_query.fetch(10)
		
class ArtistHandler(DataHandler):
	def query(self):
		artists_query = Artist.query(ancestor=musicdb.model.artist_parent_key())
		return artists_query.fetch(10)