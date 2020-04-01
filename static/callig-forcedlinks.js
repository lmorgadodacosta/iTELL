$("#add_word").on("click", function() {
    var ls = document.getElementsByName("links");
    var linksList = Array.prototype.slice.call(ls);
    var timeStamp = document.getElementById("seconds").value;
    var add = true;
    
    for (var i=0; i<linksList.length; i++) {
 				      
    	if (ls[i].value) {
            //continue;
	    ls[i].disabled = true;
        } else {
    	    //alert("Please write down a word before adding another box.");
            add = false;
         };
    };
    
    if (add) {
	$("#links_container").append("<i class='fas fa-long-arrow-alt-down'></i><input name='links' type='textarea' class='form-control form-control-lg' autocomplete='off'/>");
	$("#links_container").append("<input name='timestamps' type='hidden' value='"+ timeStamp +"'/>");
    }
});



$("#sub_button").on("click", function() {
    var ls = document.getElementsByName("links");
    var linksList = Array.prototype.slice.call(ls);
    var timeStamp = document.getElementById("seconds").value;
    $("#links_container").append("<input name='timestamps' type='hidden' value='"+ timeStamp +"'/>");
    
    for (var i=0; i<linksList.length; i++) {
        ls[i].disabled = false;
    };
    document.getElementById("forcedlinks_form").submit();
});




function countdown(seconds, tenths, elemID) {
    var e = document.getElementById(elemID);
    var g = document.getElementById("game-input");
    var s = document.getElementById("submit_button");
        
    e.innerHTML =  "Time left: " + seconds + "." + tenths + " seconds";
    
    if (seconds < 1 && tenths < 1) {
	e.innerHTML = "<input type='hidden' id='answer' name='answer' value=''><b>GAME OVER!</b><br><button type='submit' class='form-control form-control-lg btn btn-dark'>Restart</button>";
	g.innerHTML = "<input type='hidden' id='links' name='links' value=''><input name='timestamps' type='hidden' value=''/>";
	s.innerHTML = "";
	
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
