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
    startYear = ndb.StringProperty()
    
    def copy_data(self, artist_data):
        if (artist_data):
            self.canonicalName = artist_data['canonicalName']
            self.displayName = artist_data['displayName']
            self.startYear = artist_data['startYear']
    
class Venue(ModelBase):
    address = ndb.StringProperty()