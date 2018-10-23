import visionApi
import sensors
#Main function

currentRecipie = []

def ingredientSelection():
	labels 	= visionApi.getLabels
	density = sensors.getDensity

	

'''
###################################################################################
Use Google Api and existing database to figure out what ingredient has just been
added to the mixture
###################################################################################

function ingredientSelection(){ 

	function visionAPI(webcamPic){ Get tags from google
		-Send to Google vision API for labelling
		return tags;
	}
	
	function physicalProperties(sensorInfo){ Get physical ingredients
		Obtain physical properties from sensors;
		-Calculate Volume
		-Calculate Mass
		-Calculate Density
		properties = [volume, mass, density];
		return properties;
	}
	
	Search database for a ingredient approximately matching tags + physical properties
	
	ingredient = database.match([tags, properties]);	

	if(!ingredient){
		newIngredient.name = userInput();
		newIngredient.type = userInput();
		newIngredient.properties = ingredient.properties;
		newIngredient.picture = ingreident.picture;
		database.add(newIngredient);
		ingredient = newIngredient;
	}else{
		database.update(ingredient); #Update averages and add pictures
	}

	currentRecipie += currentRecipie + newIngredient;
}

###################################################################################
If the user determines the recipie, continue with the current recipie displayed
###################################################################################

function recipieSelected(recipie){ 
	
	largestMass = 0;
	intendedRatio = null;
	
	for(ingredient in currentRecipie){ #Find out which ingredients are currently in the mixture
		if(ingredient in recipie){
			recipie.ingreident.mass = currentRecipie.ingredient.mass;
			if(recipie.ingredient.mass > largestMass){
				largestMass = recipie.ingredient.mass;
				intendedRatio = recipie.ingredient.ratio; #Use the largest mass as the desired ratio
			}
		} 
	}
	
	for(ingredient in recipie){
		recipie.ingredient.massDifferential = recipie.ingredient.mass * intendedRatio.ingredient - recipie.ingredient.mass;
		
		if(recipie.ingredient.massDIfferential < 0.1 * recipie.ingredient.mass){
			#If the mass is within 10% of the intended mass it's fine
			recipie.ingredient.massDifferential = 0;
		}
	}
	
	screen.display(recipie);

	on(anyChange){
		ingredientSelection();
	}
}

###################################################################################
When the Recipie hasn't been selected, narrow down the possible recipies until 
either recipie is selected or the mix has been added
###################################################################################

while(!recipieSelected){ 
	
	on(anyChange){
		ingredientSelection();
	}

	function recipieSearch(currentRecipie){

		for(possible recipies in database){
			possibleRecipies += eachRecipie;
		}
	
		screen.display(possibleRecipies);
	}

	if(recipieSelected){
	
		recipieSelected(recipie); #Finish the recipie
	
		break; #Recipie finished
	}

	if(finished){
	
		currentRecipie.name = userInput;
		currentRecipie.ratio = smallestWholeNumberRatioOfIngredients;
	
		database.addRecipie(currentRecipie);
	}
}

###################################################################################
If the recipie has been comfirmed completed, mix it to the required viscosity
###################################################################################

function recipieCompleted(isCompleted){
	if(isCompleted){
		if(!intendedViscosity){
			FUCK;
		}
		
		function mix(intededViscosity){
			while(viscosity != intendedViscosity){
				mix;
			}
		}
	}
}
###################################################################################
Functions should be contained within their own folders. 
Everything containing:
	-Google API calls
		-Tag collection
		-Image analytics
		-Stored alongside image as a config file
	-Database functions
		-Recipie Database
			-ingredient 			#Used to determine ingredients in recipie
			-Ingredients Ratio 		#Used to determine amount of mass of each ingredient remaining
		-Ingredient Database
			-Saved
				-Density 			#Used to help identify ingredients alongside google API
				-Typical stats		#Used to help identify ingredients alongside google API
			-Set by measurements
				-mass  				#Used to help determine ingredient type and required ratio
				-Volume 			#Used to help determine ingredient type
				-mass Differential 	#Used to help determine remaining required mass
		-Image Database
			-Actual Image
			-Image stats from google
	-Webcam functions
		-Taking pictures
		-Saving and catalogging pictures
	-Sensor queries
		-Mass calculations
		-Volume calculations
		-Viscosity calculations

This file should only contain the basic flowchart of functions.
###################################################################################
'''