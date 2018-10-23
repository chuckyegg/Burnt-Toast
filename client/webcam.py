import urllib.request

#Define get image function
def getImage():
	#Temporary get image function
	#Downloads and saves an image from internet rather than taking a picture
	url = input("What is the image URL? ")
	name = input("Image name: ")

	print('Downloading file from ' + url)

	urllib.request.urlretrieve(url, '/home/pi/Programming/Burnt-Toast/temp/' + name)
	#Save the location of the image
	imageDir = '/home/pi/Programming/Burnt-Toast/temp/' + name
	#Return the directory of the image for processing
	return imageDir

'''
###################################################################################
Controls the webcam
###################################################################################
'''