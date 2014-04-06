# Model classes

import json
from google.appengine.ext import ndb

class ModelBase(ndb.Model):
    model_name = "BASE"
    canonicalName = ndb.StringProperty()
    displayName = ndb.StringProperty()
    
def artist_parent_key():
    return ndb.Key('Base', 'artist')
    
# An artist model
class Artist(ModelBase):
    model_name = 'ARTIST'
    startYear = ndb.StringProperty()
    
    def copy_data(self, artist_data):
        if (artist_data):
            self.canonicalName = artist_data['canonicalName']
            self.displayName = artist_data['displayName']
            self.startYear = artist_data['startYear']
            
def venue_parent_key():
    return ndb.Key('Base', 'venue')
    
class Venue(ModelBase):
    model_name = "VENUE"
    address = ndb.StringProperty()
    description = ndb.StringProperty()
    
    def copy_data(self, venue_data):
        if (venue_data):
            self.canonicalName = venue_data['canonicalName']
            self.displayName = venue_data['displayName']
            self.address = venue_data['address']
            self.description = venue_data['description']