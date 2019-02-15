var express 	= require('express');
var app 		= express();
var fs 			= require("fs");
cors = require('cors')(); 
app.use(cors);
var bodyParser 	= require('body-parser');
var multer 		= require('multer');
var mysql 		= require('mysql');
 var upload 		= multer();

var storage = multer.diskStorage({
    destination: (req, file, cb) => {
      cb(null, './uploads')
    },
    filename: (req, file, cb) => {
      cb(null, file.fieldname + '-' + Date.now())
    }
});

var upload = multer({storage: storage});


// const vision = require('@google-cloud/vision');
// const client = new vision.ImageAnnotatorClient({
// 		keyFilename: "/home/charles/credentials/Burnt-Toast.json"
// });

//var db 		= require('./utils/server/database.js');
//var pic 	= require('./utils/server/visionapi.js')

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "burntToast",
  database: "BURNTTOAST"
});


app.use(bodyParser.json({limit:  '50mb'})); 						
app.use(bodyParser.urlencoded({ extended: true, limit: '50mb' })); 	

// app.post('/imageLookup', upload.single("image"), async function (req, res) {
  
//     console.log(req.file);
//     console.log("image Lookup");
//     let result = await client.labelDetection(req.file.buffer);
//     labels = result[0].labelAnnotations
//     tags = []
//     labels.forEach(label => tags.push(label.description))
//     console.log(tags);
//     //db.addImage(con, 1, "test ingredient", "test tags", 1);
//     res.send(tags);
// })

app.post('/imageSubmission', upload.single("image"), async function(req, res){
  console.log("Image submission recieved")
  name = req.body.name;
  type = req.body.type;
  mass = req.body.mass;
  volume = req.body.mass;
  density = req.body.density;
  image = req.body.image;

  con.connect(function(err){
    if (err) throw err;
    console.log("Connected to MySQL");
    var sql = "INSERT INTO ingredients (name, type, mass, volume, density, image) VALUES (?, ?, ?, ?, ?, ?)";
    con.query(sql, [name, type, mass, volume, density, image], function (err, results){
      if(err){
        console.log(err);
      }
    })
    console.log("1 record inserted");
  })
  res.sendStatus(200);
})

app.post('/experimentSubmission', async function(req, res){
  console.log("Experiment Submission Recieved")
  
  var sqlIngredients = JSON.stringify({ingredients: req.body.ingredients});
  var sqlResults = JSON.stringify({results: req.body.results});
  console.log(sqlIngredients);
  console.log(sqlResults)
  con.connect(function(err){
    if (err) throw err;
    console.log("Connected to MySQL");
    var sql = "INSERT INTO experiments (ingredients, results) VALUES (?, ?)";
    con.query(sql, [sqlIngredients, sqlResults], function (err, results){
      if (err){
        console.log(err);
      }
      console.log("1 record inserted")
    })
  })
  
  res.sendStatus(200);
})


var server = app.listen(3000, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)
})

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
 