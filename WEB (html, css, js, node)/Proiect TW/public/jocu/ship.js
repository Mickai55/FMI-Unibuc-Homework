function Ship() {
  
  this.x = width/2;
  this.y = 0;
  this.img = loadImage('nava2.png');

  this.show = function() {
    fill(255);
    rectMode(CENTER);
    image(this.img, this.x - 32, this.y - 27, 65, 55);
    //rect(this.x, this.y, 20, 50, 500, 500, 3, 3);
  }

  this.move = function(dir) {
    if(mouseX > 0 && mouseX < 600)
      this.x = mouseX;
    if(mouseY > 0 && mouseY < 400)
      this.y = mouseY;
  }

}
