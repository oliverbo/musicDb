# Model classes

import json
from google.appengine.ext import ndb

class ModelBase(ndb.Model):
    model_name = "BASE"
    
class Artist(ModelBase):
    canonicalName = ndb.StringProperty()
    displayName = ndb.StringProperty()