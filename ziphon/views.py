from django.shortcuts import render_to_response
from django.template import RequestContext

from thedebaters.ziphon.forms import PersonForm

def index(request, template="ziphon/register.html", form=PersonForm):

    return render_to_response(template, {
	"form": form(),
    }, context_instance=RequestContext(request))
