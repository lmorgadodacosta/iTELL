$(function() {
    $(document).ready(function(){

	var report_div = document.getElementById("lccreport");
	report_div.innerHTML = "<div style='text-align:center; font-size: 350%;'><i class='fa fa-spinner fa-pulse fa-4x fa-fw'></i></div>";

	var msg = document.getElementById("msg");

	$.getJSON($SCRIPT_ROOT + '/_lccReport', {
	    fn: $('input[name="fn"]').val()
	}, function(data) {

	    if (data.result) {
		r = String(data.result);
		msg.innerHTML = "";
		report_div.innerHTML = r;
	    } else {
		msg.innerHTML = "";
		report_div.innerHTML = "";
		alert("Something bad happened! Please Report.");
	    }

	});

    });
});

