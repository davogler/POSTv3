from django.template import Library
from django import template
from django.db.models import get_model

from django.contrib.auth.decorators import login_required


from django.template import Context, loader
from django.http import HttpResponse
from django.template import RequestContext
import datetime

from insta.models import InstaPost
     
register = Library()
register = template.Library()


def tagged_media(request, tag):
    media = InstaPost.objects.filter(tag=tag)
    return {'media': media}
    
register.inclusion_tag('insta/tagged_media.html')(tagged_media)