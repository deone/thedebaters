from django.shortcuts import render_to_response
from django.template import RequestContext

from thedebaters.ziphon.forms import PersonForm
from thedebaters import helpers as h

@h.json_response
def index(request, template="ziphon/register.html", form=PersonForm, **kwargs):
    if request.method == "POST":
	form = form(request.POST)

	if form.is_valid():
	    person = form.save()
	    return (True, "Person Added")

	return h.dict_error(form.errors.items())

    else:
	return render_to_response(template, {
	    "form": form(),
	}, context_instance=RequestContext(request))
