module.exports.addImage = function(con, ingredient_no, ingredient_name, tags, density){
	con.connect(function(err){
		if (err) throw err;
		console.log("Connected!");
		con.query('INSERT INTO images (ingredient_no, ingredient_name, tags, density) VALUES (?, ?, ?, ?);', [ingredient_no, ingredient_name,tags,density] , function (err, result) {
			if (err) throw err;
			console.log(result);
	  	});
	});
};

/*
Containing all useful database functions

Recipie database functions
	-recipieMatch(currentRecipie)
	-recipieGetRatio(recipie)
	-recipieGetIngredients(recipie)
	-addRecipie(newRecipie)

Ingredient database functions
	-ingrdientMatch([tags, properties])
	-ingredientGetDensity(ingredient)
	-ingredientGetTags(ingredient)
	-addIngredient(newIngredient)
	-ingredientUpdate(ingredient)

Image database functions
	-addImage(image, tags)
	-setIngredient(ingredient)

This file should contain all database functions to be referenced by other modules
*/

