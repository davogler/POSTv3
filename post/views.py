from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

def custom404(request):
    return render_to_response('404.html', context_instance=RequestContext(request))
