# Base class for handlers for NDB data access

_handler_map = {}

class DataHandler:
	
	# queries all data
	def query(self):
		pass
		
	def find(self, key):
		"""Finds a record uniquely identified by key or None if the key doesn't exist"""
		pass
		
	# saves an object
	def save(self, data, key = None):
		pass
		
	def delete(self, key):
		"""Deletes a record identified by the key"""
		pass
				
	# registers a new handler
	@staticmethod
	def register(name, handler_object):
		_handler_map[name] = handler_object
		
	@staticmethod
	def get_handler(name):
		return _handler_map[name]