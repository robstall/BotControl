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
    // btn_mv down
    $(".btn_mv").mousedown(function(){
    	var id = $(this).attr('id');
        console.log("move " + id);
        switch(id) {
        	case 'FWD':
        		data = {'lspd':1,'rspd':1};
        		break;
        	case 'CCW':
        		data = {'lspd':-1,'rspd':1};
        		break;
        	case 'CW':
        		data = {'lspd':1,'rspd':-1};
        		break;
        	case 'REV':
        		data = {'lspd':-1,'rspd':-1};
        		break;
        	default:
        		console.log("unknown move id: " + id);
        		data = {'lspd':0,'rspd':0};
        		break;
        }
        post("/servo", data);
        return false;
    });

	// btn_mv up
    $(".btn_mv").mouseup(function(){
        console.log("halt");
        data = {'lspd':0,'rspd':0}
        post("/servo", data);
        return false;
    });
});

function post(url, data) {
    $.ajax({
    	type: 'POST',
    	url: url,
    	data: JSON.stringify(data, null, '\t'),
     	contentType: 'application/json;charset=UTF-8',
        success: function(response) {
        	console.log(response);
        },
   		error: function(error) {
            console.log(error);
        }
	});
}