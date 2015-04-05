from django.template import Library
from django import template
from django.db.models import get_model
from articles.models import Article, Issue
from catalog.models import Subscription
from django.contrib.auth.decorators import login_required


from django.template import Context, loader
from django.http import HttpResponse
from django.template import RequestContext
import datetime
     
register = Library()
register = template.Library()




def subscribe_button(request):
    sub = Subscription.objects.filter(is_active=1)[:1]
    context_object_name = 'sub'
    return {'sub': sub}
    
register.inclusion_tag('catalog/subscribe_button.html')(subscribe_button)