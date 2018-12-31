const express = require("express");
const app = express();
const fs = require('fs');
const bodyParser = require('body-parser');

const PORT = process.env.PORT || 5000

var points = [];

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({extended: true}));

app.use(express.static(__dirname + '/public/css'));
app.use(express.static(__dirname + '/public/vendor'));
app.use(express.static(__dirname + '/public/js'));

app.get('/',function(req,res){
  res.sendFile(__dirname+'/public/index.html');
});

app.get('/points', function(req,res){
  res.send(points);
});

app.post('/write', function(req,res){
  points.push([req.body.x, req.body.y]);
  res.sendStatus(200);
});

app.post('/erase', function(req,res){

  for (var i = 0; i<points.length; i++) {
    if( Math.sqrt(Math.pow(points[i][0] - req.body.x, 2) + Math.pow(points[i][1] - req.body.y, 2)) < 0.2 ) {
      points.splice(i,1);
    }
    res.sendStatus(200);
  }

});

app.listen(PORT);
console.log(PORT);
