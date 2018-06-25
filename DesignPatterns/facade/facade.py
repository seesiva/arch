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

	def getSummary(self):
		print ("Machine Summary")
		print ("---------------")
		print "Energy Consumption:", +self.energy.getEnergy()
		print "Produced Quantity :", +self.production.getProduction()
		print "Quality # Failed  :", +self.quality.getFailedCount()

		
class Energy:
	"""
	Subsystem for getting the energy consumption from the machine
	"""
	def getEnergy(self):
		return 40
class Production:
	"""
	Subsystem to get the units produced from the machine
	"""
	def getProduction(self):
		return 1
class Quality:
	"""
	Subsystem to track the quality aspects of the machine
	"""
	def getFailedCount(self):
	#Get the number parts produced which doesnt meet quality expectation
		return 5;		

def main():
	mymachine = Machine()
	mymachine.getSummary()

if __name__ == "__main__":
	main()
