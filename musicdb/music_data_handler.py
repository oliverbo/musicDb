# Data Handlers for Music DB

import logging
from google.appengine.ext import ndb
from eapptools.data_handler import DataHandler
import musicdb
from musicdb.music_model import Venue

MAXDATA = 50

# Handler for Artists

logger = logging.getLogger("music_data_handler")

class VenueHandler(DataHandler):
	def query(self):
		venues_query = Venue.query(ancestor=musicdb.model.venue_parent_key())
		return venues_query.fetch(MAXDATA)
	
	def save(self, data, key = None):
		"""Saves a venue. If the key does not exist, a new venue is created"""
		venue = None
		if key:
			venue = self.find(key)
		
		if not venue:
			venue = Venue(parent = musicdb.model.venue_parent_key())			
			
		venue.copy_data_and_validate(data)
		venue.put()
		
	def find(self, key):
		"""Returns a single venue identified with the key or None if it cannot be found"""
		venues_query = Venue.query(Venue.uniqueName == key)
		venues = venues_query.fetch(1)
		logger.info('Found venue for key %s: %s', key, venues)
		if (len(venues) == 0):
			return None
		else:
			return venues[0]
			
	def delete(self, key):
		venue = self.find(key)
		if venue:
			venue.key.delete()
			

			
	def export_data(self):
		return self.query()
		
	def import_data(self, data):
		logger.debug("importing %s", data)
		for venue in data:
			self.save(venue)