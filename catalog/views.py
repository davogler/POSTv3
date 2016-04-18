from django.shortcuts import render
from datetime import date
from dateutil.relativedelta import relativedelta

from catalog.models import Subscription
from articles.models import Issue



def product_list(request):
    subscriptions = Subscription.objects.all()

    issues = Issue.objects.all()

    template = "catalog/product_list.html"
    context = {"subscriptions": subscriptions, "issues": issues, }

    return render(request, template, context)


def issue_date(issue):
    issues_to_add = issue-3 #origin date = issue 3 was Jan 2014
    origin_date = date(2014, 1, 1)
    return origin_date + relativedelta(months=+(issues_to_add*2))




