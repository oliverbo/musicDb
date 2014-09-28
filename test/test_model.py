# Test for the model class

import unittest
import datetime
import json
from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed
from musicdb import music_model
	
class ModelTestCase(unittest.TestCase):
	def setUp(self):
		# First, create an instance of the Testbed class.
		self.testbed = testbed.Testbed()
		# Then activate the testbed, which prepares the service stubs for use.
		self.testbed.activate()
		# Next, declare which service stubs you want to use.
		self.testbed.init_datastore_v3_stub()
		self.testbed.init_memcache_stub()
		
	def tearDown(self):
		self.testbed.deactivate()	
		
	def testCreateEntity(self):
		# Create and store entity
		venue = music_model.Venue.create({
			'id' : 'unionpool',
			'displayName' : 'Union Pool'})
		venue_key = venue.put()
		
		venue = venue_key.get()
		
		self.assertEqual('unionpool', venue.key.id())
		self.assertEqual('Union Pool', venue.displayName)		
		
		
if __name__ == '__main__':
    unittest.main()
		
