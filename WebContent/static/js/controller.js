var cmdEnum = {
	FWD : "forward",
	FWD_RT : "forward_right",
	FWD_LF : "forward_left",
	RT: "right",
	LF: "left",
	REV: "reverse",
	REV_RT: "reverse_right",
	REV_LF: "reverse_left"
};

$(document).ready(function() {
    $(".button").mousedown(function(){
    	var id = $(this).attr('id');
        console.log("mousedown: " + id);
        return false;
    });
});

$(document).ready(function() {
    $(".button").mouseup(function(){
    	var id = $(this).attr('id');
        console.log("mouseup: " + id);
        botcmd(cmdEnum.FWD);
        return false;
    });
});

function botcmd(cmd) {
	console.log(cmd);
	var spdL = 0;
	var spdR = 0;
	switch(cmd) {
		case cmdEnum.FWD:
			spdL = 1;
			spdR = 1;
			break;
		default:
			break;
	}
	
    $.ajax({
    	url: '/servo',
    	data: { spdL : spdL, spdR : spdR },
    	dataType: "json",
        type: 'POST',
        success: function(response) {
        	console.log(response);
        },
   		error: function(error) {
            console.log(error);
        }
	});
}