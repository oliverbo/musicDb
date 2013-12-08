# Model base class

import json
from google.appengine.ext import ndb

class ModelBase(ndb.Model):
    model_name = "BASE"