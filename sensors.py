def getMass():
	mass = float(input("What is the mass? "))
	print("Mass: " + str(mass))
	return mass

def getVolume():
	volume = float(input("What is the volume? "))
	print("Volume: " + str(volume))
	return volume

def getDensity():
	mass = getMass();
	volume = getVolume();
	density = mass/volume
	print("Density: " + str(density))
	return density

getDensity()
'''
###################################################################################
This file manages all sensor readings and parsing
###################################################################################
Mass sensor
	-getMass()
	-calibrate()
	-getUncalibratedMass()
	-
###################################################################################
Volume sensor
	-getDistance()
	-getVolume()
	-calibrate()
	-
###################################################################################
Viscosity sensor
	-getViscosity()
	-
###################################################################################
'''