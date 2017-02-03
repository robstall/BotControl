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

function botcmd(cmd) {
	console.log(cmd);
    $.ajax({
    	url: '/servo',
        type: 'POST',
        success: function(response) {
        	console.log(response);
        },
   		error: function(error) {
            console.log(error);
        }
	});
}