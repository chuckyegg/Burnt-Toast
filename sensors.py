def getMass():
	mass = input("What is the mass? ")
	print("Mass: " + mass)
	return mass

def getVolume():
	volume = input("What is the volume? ")
	print("Volume: " + volume)
	return volume

def getDensity():
	mass = getMass();
	volume = getVolume();
	density = mass/volume
	print("Density: " + density)
	return Density

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