"""
Facade Pattern - Provides a unified interface to subsystems
"""
class Machine:
	"""
	Subsystem classes are responsible  for a request, so that it can be appropriately delegated to appropropriate su	sub systems.
	"""
	def __init__(self):
		self.energy=Energy()
		self.production=Production()
		self.quality=Quality()

	def Summary():
		print ("Machine Summary")
class Energy:
	"""
	Subsystem for getting the energy consumption from the machine
	"""
	def getEnergy():
		return 0
class Production:
	"""
	Subsystem to get the units produced from the machine
	"""
	def getProduction():
		return 1
class Quality:
	"""
	Subsystem to track the quality aspects of the machine
	"""
	def getFailedCount():
	#Get the number parts produced which doesnt meet quality expectation
		return 5;		
