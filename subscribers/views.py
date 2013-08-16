from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from subscribers.models import *
import post.settings as settings
from django.http import HttpResponse, HttpResponseRedirect
from subscribers.helium import Helium
import datetime

def get_subscriber(request):
    h = Helium(settings.HELIUM_API_KEY)
    data = h.get_charges()
    
    splifflist=[]
    for obj in data:
        splifflist.append(obj['customer']['email'])
        obj, created = Subscriber.objects.get_or_create(
            email = obj['customer']['email'],
            cust_id = obj['customer']['id'],
            name = obj['customer']['address']['recipient'],
            street = obj['customer']['address']['street'],
            city = obj['customer']['address']['city'],
            state = obj['customer']['address']['state'],
            zip = obj['customer']['address']['zipcode'],
            charge_id = obj['id'],
            charge_date = datetime.datetime.fromtimestamp(obj['created']),
            expires_on = datetime.datetime.fromtimestamp(obj['created']) + datetime.timedelta(days=365)
            )
        
    
    
    
    if 'HTTP_REFERER' in request.META:
      return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
      return HttpResponseRedirect('/')    
    
