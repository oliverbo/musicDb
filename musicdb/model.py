# Model classes

import json
from google.appengine.ext import ndb

class ModelBase(ndb.Model):
    model_name = "BASE"
    uniqueName = ndb.StringProperty()
    displayName = ndb.StringProperty()
    
def artist_parent_key():
    return ndb.Key('Base', 'artist')
    
# An artist model
class Artist(ModelBase):
    model_name = 'ARTIST'
    startYear = ndb.StringProperty()
    
    def copy_data(self, artist_data):
        if (artist_data):
            self.uniqueName = artist_data['uniqueName']
            self.displayName = artist_data['displayName']
            self.startYear = artist_data['startYear']
            
def venue_parent_key():
    return ndb.Key('Base', 'venue')
    
class Venue(ModelBase):
    model_name = "VENUE"
    address = ndb.StringProperty()
    zipCode = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    neighborhood = ndb.StringProperty()
    website = ndb.StringProperty()
    twitterName = ndb.StringProperty()
    facebookURI = ndb.StringProperty()
    phoneNumber = ndb.StringProperty()
    priceLevel = ndb.IntegerProperty()
    specialTip = ndb.StringProperty()
    description = ndb.StringProperty()
    capacity = ndb.IntegerProperty()
    booking = ndb.StringProperty()
    
    def copy_data(self, venue_data):
        if (venue_data):
            self.uniqueName = venue_data['uniqueName']
            self.displayName = venue_data['displayName']
            self.address = venue_data['address']
            self.zipCode = venue_data['zipCode']
            self.city = venue_data['city']
            self.neighborhood = venue_data['neighborhood']
            self.website = venue_data['website']
            self.twitterName = venue_data['twitterName']
            self.facebookURI = venue_data['facebookURI']
            self.phoneNumber = venue_data['phoneNumber']
            self.priceLevel = int(venue_data['priceLevel'])
            self.description = venue_data['description']
            self.capacity = int(venue_data['capacity'])
            self.booking = venue_data['booking']