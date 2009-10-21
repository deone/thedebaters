from django.shortcuts import render_to_response
from django.template import RequestContext

def login(request, template="accesscard/login.html"):

    return render_to_response(template, {}, context_instance=RequestContext(request))
