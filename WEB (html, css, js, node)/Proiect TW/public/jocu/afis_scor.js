function apasa() {
    
    
    $.get( "/get", function(data) {
        // alert("DA")

        data.sort(function(a, b){return a.scor_jucator - b.scor_jucator})

        $("p").append("HighScores:" + "<br><br>")
        $("p").append("Locul 1: " + data[data.length - 1].scor_jucator + "<br>")
        $("p").append("Locul 2: " + data[data.length - 2].scor_jucator + "<br>")
        $("p").append("Locul 3: " + data[data.length - 3].scor_jucator + "<br>")
      
        // document.getElementById("odata").onclick = null;
        document.getElementById("odata").style.display = "none";
        document.getElementById("odata2").style.display = "none";
        button.hide();

    });
}

function apasa2(){
    // alert("nu")
    document.getElementById("odata2").style.display = "none";
  }


