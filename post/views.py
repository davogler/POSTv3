from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

def custom404(request):
    
    response = render_to_response('404.html', locals(), context_instance=RequestContext(request))
    response.status_code = 404
    return response
