// var myTabs = new tabs(document.getElementById("tabs"), "article", "h2").responsive("myTabs", { prev: "Previous", next: "Next" });

window.onbeforeunload = () => {
    window.scrollTo(0, 0)

}

function tabs(a, g, j) {
    document.body.className = "js-on";
    
    var g = a.getElementsByTagName(g),
        d = [],
        c;
    this.active;
    this.total = g.length;
    this.container = a;

    e = a.insertBefore(document.createElement("nav"), g[0]), change = function (f) {
        window.scrollTo(0, 0);
        if (typeof this.active !== "undefined") {
            d[this.active].className = g[this.active].className = ""
        }
        d[f].className = g[f].className = "active";
        this.active = f
    }, clickEvent = function (h, f) {
        h.onclick = function () {
            change(f);
            return false
        }
    };

    for (var b = 0; b < g.length; b++) {
        d[b] = e.appendChild(document.createElement("a"));
        d[b].href = "#";
        c = [g[b].getAttribute("data-title"), g[b].getElementsByTagName(j)[0]];
        d[b].innerHTML = c[0] !== null ? c[0] : c[1] ? c[1]["innerText" || "textContent"] : b + 1;
        new clickEvent(d[b], b)
    }
    change(0)
}

tabs.prototype.change = function (b) {
    change(b - 1)
};

tabs.prototype.next = function (b) {
    active === this.total - 1 ? change(0) : change(active + 1)
};

tabs.prototype.prev = function (b) {
    active === 0 ? change(this.total - 1) : change(active - 1)
};

//cand e micsorat

tabs.prototype.responsive = function (d, c) {
    nav = document.createElement("nav");
    nav.id = "mobiles";
    nav.innerHTML = '<a href="#" onclick="' + d + '.prev(); return false">' + c.prev + '</a><a href="#" onclick="' + d + '.next(); return false">' + c.next + "</a>";
    this.container.insertBefore(nav, this.container.firstChild);
    return this
};


// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img =  [document.getElementById("img1"), document.getElementById("img2"), document.getElementById("img3"), 
            document.getElementById("img4"), document.getElementById("img5"), document.getElementById("img6"), 
            document.getElementById("img7"), document.getElementById("img8"), document.getElementById("img9"), 
            document.getElementById("img10"), document.getElementById("img11"), document.getElementById("img12")];
var modalImg = document.getElementById("img01");

for(var i = 0; i < img.length; i++)
    img[i].onclick = function(){
        modal.style.display = "block";
        modalImg.src = this.src;
    }

var span = document.getElementsByClassName("close")[0];

span.onclick = function() { 
    modal.style.display = "none";
}

// Mars

function schimbareSursaImg() {
    if (document.getElementById('imgM1').src == 'http://localhost:3000/stylesheets/images/mars1.jpg')
        document.getElementById('imgM1').src='http://localhost:3000/stylesheets/images/mars2.jpg'
    else
    document.getElementById('imgM1').src='http://localhost:3000/stylesheets/images/mars1.jpg'
}

function pixeliRandomImg() {
    img = document.getElementById("patrat")
    r = Math.floor(Math.random() * 256);
    g = Math.floor(Math.random() * 256);
    b = Math.floor(Math.random() * 256);

    img.style.backgroundColor = "rgb(" + r + "," + g + "," + b + ")"

    bgc = window.getComputedStyle(img, null).getPropertyValue("background-color");

    document.getElementById("bgc").innerHTML = bgc
}

function informatii() {
    var para = document.createElement("P");
    para.innerHTML = "Marte este, pornind dinspre Soare, a patra planetă a Sistemului Solar, a cărei denumire provine de la Marte, zeul roman al războiului. Uneori mai este numită și „planeta roșie” datorită înfățișării sale văzută de pe Pământ. Culoarea roșiatică se explică prin prezența pe suprafața sa a oxidului de fier.";
    document.getElementById("inf").appendChild(para);
}

function delInformatii() {
    var list = document.getElementById("inf");
    list.removeChild(list.childNodes[0]);
}

function schimbareClasa() {
	document.getElementById("patrat").className = "patratClass";
}

function colorareButoane() {
  var c = document.getElementById("mars").children;
  var i;
  for (i = 0; i < c.length; i += 2) {
  	if (c[i].style.backgroundColor == "red")
    	c[i].style.backgroundColor = "";
    else
    	c[i].style.backgroundColor = "red";
  }
  for (i = 1; i < c.length; i += 2) {
  	if (c[i].style.backgroundColor == "")
    	c[i].style.backgroundColor = "green";
    else
    	c[i].style.backgroundColor = "";	
  }
}

document.getElementById("pp").addEventListener("click", function() {
    alert("You clicked the P element!");
}, true);

document.getElementById("form").addEventListener("click", function() {
    alert("You clicked the FORM element!");
}, true);

document.getElementById("dv").addEventListener("click", function() {
    alert("You clicked the DIV element!");
}, true);
  

var myTextbox = document.getElementById('input');
myTextbox.addEventListener('keypress', checkName, false);

function checkName(evt) {
    var charCode = evt.charCode;
    if (charCode != 0) 
      if (charCode < 97 || charCode > 122) 
        evt.preventDefault();
}

function submit() {
    var x = document.getElementById("input").value;
    x = x.toUpperCase()
    document.getElementById("salut").innerHTML = "Bună " + x + "!";
    document.getElementById("salutcit").innerHTML = ""
}

function citireLit(event) {
    var x = event.key;
    document.getElementById("salutcit").innerHTML = "The pressed key was: " + x;
}

function clickCounter() {
    if (typeof(Storage) !== "undefined") {
        if (localStorage.clickcount) {
            localStorage.clickcount = Number(localStorage.clickcount)+1;
        } else {
            localStorage.clickcount = 1;
        }
        document.getElementById('butonulMagic').innerHTML = "De când există, acest buton a fost apăsat de " + localStorage.clickcount + " ori!!";
    }
}

function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("mars").innerHTML = this.responseText;
      }
    };
    xhttp.open("GET", "doc.txt", true);
    xhttp.send();
  }