var express = require('express');
var app = express();
var fs = require("fs");

//Todo:
  //Ingredient Loopup
    //Google API lookup
    //Database Lookup
    //If known Return actual ingredient
    //Otherwise ask for confirmation
  //Recipie Get
    //Using current composition get a list of recipies
  //Ingredient Add
    //Add ingredient to database

app.get('/listUsers', function (req, res) {
    console.log("listUsers");
    res.end("test");    
})

var server = app.listen(3000, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)
})
