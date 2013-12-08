# Artist data model

from google.appengine.ext import ndb
from modelbase import ModelBase

class Artist(ModelBase):
    canonical_name = ndb.StringProperty()
    display_name = ndb.StringProperty()
    
