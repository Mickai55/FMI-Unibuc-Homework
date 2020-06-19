var ship;
var flowers = [];
var drops = [];
var numberOfFlowers = 0;
var index = 0;
var shooting_delay = 7;
var score = 0; // asta trebuie afisat in JSON
var texts;
let img;
var speed = 2;
var stop = 1;
var sw = 0;

function preload() {
  img = loadImage('bg1.jpg');
}

function setup() {
  createCanvas(600, 400);
  ship = new Ship();
  texts = new Text();
  createFlowers();
}

function draw() {
  // background(51);
  image(img, 0, 0, 600, 400);
  
  if (stop == 1 && sw == 0){

    fButton("START");
    button.mousePressed(startGame);
    sw = 1;
  }

  if(stop == 0){

    var edge = false;
    var left_edge = false;
    
    ship.show();
    ship.move();
    shooting();
    hitting();
    texts.score = score;
    texts.score_show();

    for (var i = 0; i < flowers.length; i++) {
      flowers[i].show();
      flowers[i].move();
      if (flowers[i].x + flowers[i].r > width || flowers[i].x - flowers[i].r < 0) {
        edge = true;
      }

      if (flowers[i].x - flowers[i].r < 0)
        left_edge = true;
    }

    if (edge) {
      for (var i = 0; i < flowers.length; i++)
        flowers[i].shiftDown();
    }

    if (left_edge) {
      createFlowers();
    }

    for (var i = drops.length-1; i >= 0; i--) {
      if (drops[i].toDelete) {
        drops.splice(i, 1);
      }
    }
    
    for (var i = 0; i < numberOfFlowers; i++)
      if(flowers[i].r != -1 && flowers[i].y > 300)
        stop = 2; 
  }
  else if(stop == 2){// GAME OVER

    document.getElementById("hiddenscor").value = score;
    noLoop();

    sw = 0;
    flowers = [];
    numberOfFlowers = 0;
    createFlowers();
    speed = 2;
    score = 0;
    
    ship.x = 1000;
    texts.score_show();
    texts.lost();

    if (stop == 2 && sw2 == 0){
      fButton("PLAY AGAIN");
      button.mousePressed(startGame);
      sw2 = 1;
    }
    
  }
}

function createFlowers() {
  for (var i = 0; i < 7; i++) {
    flowers[numberOfFlowers] = new Flower(i * 70 + 30, 50);
    numberOfFlowers++;
  }

  if(numberOfFlowers != 7)
    speed += 0.1;

  for (var i = 0; i < numberOfFlowers; i++) 
    flowers[i].speed = speed;
}

function shooting() {
  if(mouseIsPressed) 
    index++;
  else
    index = 0;
  if(index % shooting_delay == 1){
    var drop = new Drop(ship.x, ship.y - 25);
    drops.push(drop);
  }
}

function hitting() {

  for (var i = 0; i < drops.length; i++) {
    drops[i].show();
    drops[i].move();
    for (var j = 0; j < flowers.length; j++) {
      if (drops[i].hits(flowers[j])) {
        flowers[j].shrink();
        drops[i].evaporate();
      }
    }
  }
  
}

function fButton(x) {
  button = createButton(x);
  button.position(215, 215);
  button.style("height","100px");
  button.style("width","200px");
  button.style("font-size","40px");
  button.style("font-family","Times New Roman");
  button.style("background-color","black");
  button.style("color","white");
}

function startGame() {
  stop = 0;
  button.hide();
  sw2 = 0;
  loop();
}