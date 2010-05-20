var options = {
    url: null,
    type: "POST",
    data: null,
    dataType: "json",
    success: null,
    error: function(response)	{
	alert(response);
    }
}

function savePerson()	{
    firstName = $("#id_first_name").val();
    lastName = $("#id_last_name").val();
    sex = $("#id_sex").val();
    homePhone = $("#id_home_phone").val();
    officePhone = $("#id_office_phone").val();
    mobilePhone = $("#id_mobile_phone").val();
    email = $("#id_email").val();
    address = $("#id_address").val();
    dateOfBirth = $("#id_date_of_birth").val();
    stateOfOrigin = $("#id_state_of_origin").val();
    relationshipStatus= $("#id_relationship_status").val();
    occupation = $("#id_occupation").val();
    hobbies = $("#id_hobbies").val();

    options["url"] = "/register";
    options["data"] = "first_name=" + firstName +
			"&last_name=" + lastName +
			"&sex=" + sex +
			"&home_phone=" + homePhone +
			"&office_phone=" + officePhone +
			"&mobile_phone=" + mobilePhone +
			"&email=" + email +
			"&address=" + address +
			"&date_of_birth=" + dateOfBirth +
			"&state_of_origin=" + stateOfOrigin +
			"&relationship_status=" + relationshipStatus +
			"&occupation=" + occupation +
			"&hobbies=" + hobbies;
    options["success"] = function(response) {
	alert(response);
    }

    $.ajax(options);
}
