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
from django.template.loader import get_template

register = Library()
register = template.Library()


def subscribe_button(request):
    sub = Subscription.objects.filter(is_active=1).filter(type=1)[:1]
    context_object_name = 'sub'
    return {'sub': sub}

register.inclusion_tag('catalog/subscribe_button.html')(subscribe_button)


def now_accepting(request):
    sub = Subscription.objects.filter(is_active=1).filter(type=1)[:1]
    context_object_name = 'sub'
    return {'sub': sub}

register.inclusion_tag('catalog/now_accepting.html')(now_accepting)

@register.assignment_tag
def get_latest_issue():
    latest_issue = Subscription.objects.filter(is_active=1).filter(type=1).latest('first_issue')
    return latest_issue

@register.assignment_tag
def get_next_latest_issue():
    next_latest_issue = Subscription.objects.filter(is_active=1).filter(type=1).order_by('-first_issue')[1]
    return next_latest_issue
