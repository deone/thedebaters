function ajaxPost(url, data, dLocation)  {

    $.ajax({
        url: url,
        type: "POST",
        data: data,
        dataType: "json",

        success: function(response) {
            if (response.code != 0) {
		showMessage("Internal Server Error");
            } else  {
                if (response.data.type == "error")  {
		    if (!response.data.body.keys)   {
			showMessage(response.data.body["__all__"]);
		    } else  {
			highlightErrorFields(response.data.body);
			showMessage("Please fill out required fields");
		    }
                } else  {
                    document.location = dLocation;
                }
            }
        },

        error: function(response)   {
	    showMessage("Internal Server Error");
        }
    });

}

function login()    {

    var pin = $("#id_pin").val();
    var serial_no = $("#id_serial_no").val()

    var data = "pin=" + pin + "&serial_no=" + serial_no;
    var url = "/";
    var dLocation = "/apply/";

    ajaxPost(url, data, dLocation);

}
