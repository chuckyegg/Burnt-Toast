const serialPort = require('serialport')
var express 	= require('express');
var app 		= express();
var bodyParser 	= require('body-parser');
//const Readline = require('@serialport/parser-readline')

app.use(bodyParser.json()); 						
app.use(bodyParser.urlencoded({ extended: true }));

var serialArray = [];

const port = new serialPort('COM3',{
    baudRate: 115200,
    autoOpen: false
}, function (err){
    if (err){
        return console.log('Error:', err.message);
    }
})
//const parser = port.pipe(new Readline({ delimiter: '\r\n' }))
//parser.on('readable', console.log)
port.on('data',function(data){
    serialArray.push(data.toString('utf8'));
    console.log(data.toString('utf8'));
})

app.post('/start', async function(req, res){
    console.log("Starting Serial");
    res.send("Starting Serial");
    port.open(function(err){
        if(err){
            return console.log(err.message);
        }
    })
})

app.post('/stop', async function(req,res){
    console.log("Stopping Serial")
    port.close(function(err){
        if(err){
            return console.log(err.message);
        }
    })
    res.send(serialArray);
    console.log(serialArray);
    serialArray = [];
})

app.get('/', async function(req, res){
    res.sendFile('/index.html', {root: __dirname});

})

app.get('/webcam.min.js', async function(req, res){
    res.sendFile('/node_modules/webcamjs/webcam.min.js', {root:__dirname})
})

var server = app.listen(3000, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)
})