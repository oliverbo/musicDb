# Data Handlers for Music DB

import logging
from apptools.data_handler import DataHandler
import musicdb
from musicdb.model import Artist
from musicdb.model import Venue

# Handler for Artists

logger = logging.getLogger("music_data_handler")

class VenueHandler(DataHandler):
	def query(self):
		venues_query = Venue.query(ancestor=musicdb.model.venue_parent_key())
		return venues_query.fetch(10)
	
	def save(self, data):
		venue = Venue(parent = musicdb.model.venue_parent_key())
		venue.copy_data(data)
		venue.put()
		
class ArtistHandler(DataHandler):
	def query(self):
		artists_query = Artist.query(ancestor=musicdb.model.artist_parent_key())
		return artists_query.fetch(10)
		
	def save(self, data):
		artist = Artist(parent = musicdb.model.artist_parent_key())
		artist.copy_data(data)
		artist.put()