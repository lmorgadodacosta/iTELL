function countdown(seconds, tenths, elemID) {
    var e = document.getElementById(elemID);
    var g = document.getElementById("game-input");
    e.innerHTML =  "Time left: " + seconds + "." + tenths + " seconds";

    if (seconds < 1 && tenths < 1) {
	e.innerHTML = "<input type='hidden' id='answer' name='answer' value=''><b>GAME OVER!</b><br><button type='submit' class='form-control form-control-lg btn btn-dark'>Restart</button>";
	g.innerHTML = "<input type='hidden' id='answer' name='answer' value=''>";
			      // setTimeout(location.reload(),2000);
			      //clearTimeout(timer);
			      // check();
			      // do stuff here
    } else {
        if (tenths < 1) {
	    seconds--;
	    tenths = 9;
        } else {
            tenths--;
        }
        var timer = setTimeout('countdown('+seconds+', '+tenths+',"'+elemID+'")',100);
    }
}		 


function countup(seconds, tenths, elemID) {
    var e = document.getElementById(elemID);
    e.innerHTML =  "Time spent: " + seconds + "." + tenths + " seconds";

    if (tenths < 9) {
	tenths++;
    } else {
	tenths = 0;
	seconds++;
    }
    var timer = setTimeout('countup('+seconds+', '+tenths+',"'+elemID+'")',100);
}		 


function countseconds(seconds, tenths, elemID) {
    //var e = document.getElementById(elemID);
    var he = document.getElementById("seconds");
    //e.innerHTML =  "Time spent: " + seconds + "." + tenths + " seconds";
    he.value = seconds + "." + tenths

    if (tenths < 9) {
	tenths++;
    } else {
	tenths = 0;
	seconds++;
    }
    var timer = setTimeout('countseconds('+seconds+', '+tenths+',"'+elemID+'")',100);
}		 
