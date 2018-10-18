#Import modules to read from drive
import io
import os

#Import custom webcam module to take picture with webcam
import webcam

#Import Google Cloud Vision Modules
from google.cloud import vision
from google.cloud.vision import types

#Initalise Google Vision client
client = vision.ImageAnnotatorClient()

#Define the get labels function
def getLabels():
	#Recieve image from webcam
	imageDir = webcam.getImage()

	fileName = os.path.join(
		os.path.dirname(__file__),
		imageDir)

	with io.open(fileName, 'rb') as imageFile:
		content = imageFile.read()

	image = types.Image(content=content)

	labelResponse = client.label_detection(image=image)
	propertyResponse = client.image_properties(image=image)

	properties = propertyResponse.image_properties_annotation
	labels = response.label_annotations
	#Return an array of labels from the vision API
	print("Properties: " + properties)
	print("Labels: " + labels)

getLabels()

'''
###################################################################################
This file manages google vision api
###################################################################################
vision
	-get labels
	-get information
	-get whatever
###################################################################################
'''