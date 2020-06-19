function Flower(x, y) {
  this.x = x;
  this.y = y;
  this.r = 30;
  this.intensity = 200;
  this.speed;

  this.xdir = 1;

  this.shrink = function() { 
    this.intensity -= 50;
    if (this.intensity == 0) {
      this.r = -1;
      score += 10;
    }
  }

  this.shiftDown = function() {
    this.xdir *= -1;
    this.y += 35;
  }

  this.move = function() {
    this.x = this.x + (this.xdir * this.speed);
  }

  this.show = function() {
    noStroke();
    fill(12, 143, 0, this.intensity);
    ellipse(this.x, this.y, this.r*2, this.r*2);
  }

}
