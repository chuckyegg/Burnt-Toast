import urllib.request

def getImage():
	
	url = input("What is the image URL?")
	name = input("Image name")
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