#Class file for server and client to use

def ingredient: #Ingredient class, contains all ingredient information pre and post database search
	__init__(self, mass, volume, image):
		self.mass = mass			#Set the mass given by sensors
		self.volume = volume		#Set the volume given by sensors
		self.density = mass/volume	#Calculate the density given by sensors
		self.image = image			#Send the webcam image for processing
		
def recipe:
	ratio = []
	ingredients = []

def composition:
	ingredients = []
	recipe = []
	
def request:
	__init__(self, requestType, ingredient):
		self.requestType = requestType
		self.ingredient = ingredient

		