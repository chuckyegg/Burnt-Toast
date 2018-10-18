import urllib.request

def getImage():
	
	url = raw_input("What is the image URL?")
	name = raw_input("Image name")
	print('Downloading file from ' + url)

	urllib.request.urlretrieve(url, '/home/pi/Programming/Burnt-Toast/temp/' + name)

getImage()
'''
###################################################################################
Controls the webcam
###################################################################################
Webcam functions
	-takePicture()
###################################################################################
'''