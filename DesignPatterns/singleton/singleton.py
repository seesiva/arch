"""
Singleton design pattern is used when we are dealing with an situation where in there is a need for access to only one instance for global access. Typically would be very suitable for handling configuration
"""
class Configuration:
	__instance = None
	
	@staticmethod
	def getConfiguration():
		""" Static access method. """
		if Configuration.__instance == None:
			Configuration()
		return Configuration.__instance
	
	def __init__(self):
		if Configuration.__instance != None:
			raise Exception("This is a singleton")
		else:
			Configuration.__instance = self

# instantiate a configuration once
c = Configuration()
print c # Prints the instance
#d = Configuration() This would raise an exception

d = Configuration.getConfiguration() # Will retrieve the same configuration
print d
