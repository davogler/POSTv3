from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from signups.forms import *
from signups.models import *
import post.settings as settings
from mailsnake import MailSnake
import json
from django.http import HttpResponse, HttpResponseRedirect
from signups.helium import Helium
import datetime

def connect(request):
  ms = MailSnake(settings.MAILCHIMP_API_KEY)
  lists = ms.lists()
  if request.method == 'POST':
    form = ConnectForm(request.POST)
    message = 'the sky is falling'
    if form.is_valid():
      ms.listSubscribe(
          id = lists['data'][0]['id'],
          email_address = (form.cleaned_data['email_signup']),
          update_existing = True,
          double_optin = False,
      )
      
      #ms.listStaticSegmentMembersAdd(
      #    id = lists['data'][0]['id'],
      #    seg_id = 157, #Fake Development People... kill this in production!
      #    batch = {
      #        'email_address': form.cleaned_data['email_signup']
      #        },
      #)
      
      
      if request.is_ajax(): #success with js
          message = 'success!'
          status = True
          return HttpResponse(json.dumps({'message':message, 'status':status}), 'application/json')
      else: #success with no js
          return redirect('success') 
    else:
      if request.is_ajax(): #error with js
          message = 'Invalid email address'
          status = False
          return HttpResponse(json.dumps({'message':message, 'status':status}), 'application/json')
      else: # error with no js
          form.addError('Invalid email address')  
  else:
    form = ConnectForm()
  
  
  return render_to_response(
    'signups/connect.html',
    {
      'form': form,
   
    },
    context_instance=RequestContext(request)
  )


def success(request):
    return render_to_response('signups/success.html', context_instance=RequestContext(request))

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
    
  