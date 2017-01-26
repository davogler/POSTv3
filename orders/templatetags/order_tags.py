from django.template import Library
from django import template
from django.db.models import get_model
from django.contrib.auth.decorators import login_required
from django.template import Context, loader
from django.http import HttpResponse
from django.template import RequestContext
from django.core.exceptions import MultipleObjectsReturned
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from django.db.models import Max

from cart.models import Cart, CartItem
from orders.models import Order, Record
from customers.models import Recipient, CreditCard


register = Library()
register = template.Library()

def checkout_ccs(request, paygo):
    user = request.user
    cclist = CreditCard.objects.filter(user=user)
    return {'cclist': cclist,
            'paygo': paygo,
            }

register.inclusion_tag('orders/checkout_creditcards.html')(checkout_ccs)

def dashboard_ccs(request):
    user = request.user
    cclist = CreditCard.objects.filter(user=user)
    return {'cclist': cclist}

register.inclusion_tag('orders/dashboard_creditcards.html')(dashboard_ccs)

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
    records = Record.objects.filter(originating_order__in=orderlist).order_by('recipient', '-timestamp')
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
def get_season(issue):
    if issue != None:
        #season will attach to issue middle month (jan, mar, jun, or sep)
        issue_19 = datetime.date(2016, 10, 1)  # issue 19 is oct 2016
        months = (issue-19)*3
        issue_delta = relativedelta(months=months)
        season_midmonth = issue_19 + issue_delta #date object
        if season_midmonth.month == 1:
            season = "Winter"
        elif season_midmonth.month == 4:
            season = "Spring"
        elif season_midmonth.month == 7:
            season = "Summer"
        elif season_midmonth.month == 10:
            season = "Fall"
        else:
            season = "Special"
    else:
        season = None

    return season

@register.assignment_tag
def get_year(issue):
    if issue != None:
        # get year of issue to go with season
        #season will attach to issue middle month (jan, mar, jun, or sep)
        issue_19 = datetime.date(2016, 10, 1)  # issue 19 is oct 2016
        months = (issue-19)*3
        issue_delta = relativedelta(months=months)
        season_midmonth = issue_19 + issue_delta #date object
    else:
        season_midmonth = None

    return season_midmonth



@register.assignment_tag
def get_first_month(issue):
    if issue != None:
        issue_3 = datetime.date(2014, 1, 1)  # issue 3 is jan 2014
        months = (issue - 3) * 2
        issue_delta = relativedelta(months=months)
        first_month = issue_3 + issue_delta
    else:
        first_month = None

    return first_month


@register.assignment_tag
def get_second_month(issue):
    if issue != None:
        issue_3 = datetime.date(2014, 1, 1)  # issue 3 is jan 2014
        months = (issue - 3) * 2 + 1
        issue_delta = relativedelta(months=months)
        second_month = issue_3 + issue_delta
    else:
        second_month = None

    return second_month


@register.assignment_tag
def get_active_status(first_month):
    now = date.today()
    if now > first_month:
        return False
    else:
        return True


@register.assignment_tag
def get_dat_cc(user):
    try:
        cc = CreditCard.objects.get(user=user, default=True)
    except MultipleObjectsReturned:
        cc = CreditCard.objects.filter(user=user)[0]
    except:
        cc = None
    return cc


@register.assignment_tag
def get_auto_renew(record):
    try:
        cart = record.originating_order.cart
        recipient = record.recipient
        cart_item = CartItem.objects.get(cart=cart, recipient=recipient)
        if cart_item.auto_renew:
            auto = True
        else:
            auto = False
    except:
        auto = None
    return auto


@register.assignment_tag
def dolla_discount(order):
    cart = order.cart
    print cart.total
    print order.total
    return (cart.total - order.total)
