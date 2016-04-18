from django.template import Library
from django import template
from django.db.models import get_model
from django.contrib.auth.decorators import login_required


from django.template import Context, loader
from django.http import HttpResponse
from django.template import RequestContext
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from django.db.models import Max


from orders.models import Order, Record
from customers.models import Recipient


register = Library()
register = template.Library()


def dashboard_orders(request):
    user = request.user
    orderlist = Order.objects.filter(user=user).exclude(status="Started").exclude(status="Pending")

    return {'orderlist': orderlist}

register.inclusion_tag('orders/dashboard_orders.html')(dashboard_orders)


def dashboard_recips(request):
    user = request.user
    reciplist = Recipient.objects.filter(user=user)

    return {'reciplist': reciplist}

register.inclusion_tag('customers/dashboard_recips.html')(dashboard_recips)


def dashboard_issue_term(request):
    user = request.user

    orderlist = Order.objects.filter(user=user).exclude(status="Started").exclude(status="Pending")
    recipients = Recipient.objects.filter(user=user)
    records = Record.objects.filter(originating_order__in=orderlist)
    # recrods  found in orderlist

    return {'orderlist': orderlist,
            'recipients': recipients,
            'records': records,
            }

register.inclusion_tag('orders/dashboard_issue_term.html')(dashboard_issue_term)

@register.assignment_tag
def get_current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.assignment_tag
def get_first_month(issue):
    issue_3 = datetime.date(2014, 1, 1) # issue 3 is jan 2014
    months = (issue - 3) * 2
    issue_delta = relativedelta(months=months)
    first_month = issue_3 + issue_delta

    return first_month

@register.assignment_tag
def get_second_month(issue):
    issue_3 = datetime.date(2014, 1, 1) # issue 3 is jan 2014
    months = (issue - 3) * 2 +1
    issue_delta = relativedelta(months=months)
    second_month = issue_3 + issue_delta

    return second_month

@register.assignment_tag
def get_active_status(first_month):
    now = date.today()
    if now > first_month:
        return False
    else:
        return True

   

