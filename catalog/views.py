from django.shortcuts import render
from catalog.models import Subscription
from articles.models import Issue



def product_list(request):
    subscriptions = Subscription.objects.all()

    issues = Issue.objects.all()

    template = "catalog/product_list.html"
    context = {"subscriptions": subscriptions, "issues": issues, }

    return render(request, template, context)
