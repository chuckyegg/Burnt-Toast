import io
import os

import webcam

from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

imageDir = webcam.getImage()

print(imageDir + ' Testing')

fileName = os.path.join(
	os.path.dirname(__file__),
	imageDir)

with io.open(fileName, 'rb') as imageFile:
	content = imageFile.read()

image = types.Image(content=content)

response = client.label_detection(image=image)
labels = response.lanel_annotations

print('Labels:')
for label in labels:
	print(label.description)

'''
###################################################################################
This file manages google vision api
###################################################################################
vision
	-get tags
	-get information
	-get whatever
###################################################################################
'''