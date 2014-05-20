# Handlers NDB data access

_handler_map = {}

class DataHandler:
	
	# queries all data
	def query(self):
		pass
		
	# saves an objec
	def save(self, data):
		pass
				
	# registers a new handler
	@staticmethod
	def register(name, handler_object):
		_handler_map[name] = handler_object
		
	@staticmethod
	def get_handler(name):
		return _handler_map[name]