function Text(score) {

    this.score = score;
    this.font = loadFont('SPACEMAN.ttf');

    this.title_show = function(){
        
    }

    this.score_show = function() {
        
        textSize(20);
        textFont(this.font);
        textAlign(RIGHT);
        fill(255, 255, 0);

        text("Score: ", 585, 350);
        text(this.score, 565, 370);
    }

    this.lost = function() {
        
        textSize(40);
        textFont(this.font);
        textAlign(CENTER);
        fill(255, 0, 0);

        text("GAME OVER!", 300, 100)
    }

}