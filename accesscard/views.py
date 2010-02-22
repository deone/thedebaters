from django.shortcuts import render_to_response
from django.template import RequestContext

from accesscard.forms import AccessForm
from thedebaters import helpers as h

def dict_error(errors):
    error_dict = {}
    keys = []

    for k, v in errors:
        error_dict[k] = v
        keys.append(k)

    if keys != ["__all__"]:
        error_dict["keys"] = keys

    return error_dict

@h.json_response
def login(request, form_class=AccessForm, template="accesscard/login.html", **kwargs):
    if request.method == "POST":
	form = form_class(request.POST)

	print form.is_valid()

    else:
	form = form_class()

	return render_to_response(template, {
	    "form": form,
	}, context_instance=RequestContext(request))
