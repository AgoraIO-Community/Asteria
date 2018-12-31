var ctx = document.getElementById('canvas').getContext('2d');
ctx.fillStyle = "#FF0000";
var points=[];

setInterval(function() {
  axios.get('points')
  .then(function(res) {
    points = res.data;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    points.forEach(function(e) {
      ctx.fillRect(e[0]*canvas.width, canvas.height - e[1]*canvas.height, 5, 5);
    });

  });
}, 100);
