# common tools

import json

# Converts a NDB object to JSON
def ndb_to_json(obj):    
	return json.dumps(obj, default = lambda o: o.to_dict())