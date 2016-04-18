from django.template import Library
from django import template
from django.template import Library, Node, Variable, loader
from django.template.context import Context
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from django.db.models import Max


from orders.models import Order, Record
from customers.models import Recipient


register = Library()
register = template.Library()



@register.assignment_tag
def get_recip_status(recipient_id):
    now = date.today()
    recipient = Recipient.objects.get(id=recipient_id)
    
    last_issue = Record.objects.filter(recipient=recipient).aggregate(Max('issue'))['issue__max']
    print "last issue is %s" % last_issue

    if last_issue is not None:
        issue_3 = datetime.date(2014, 1, 1) # issue 3 is jan 2014
        month_delta = (last_issue - 3) * 2 +1
        issue_delta = relativedelta(months=month_delta)
        second_month = issue_3 + issue_delta

        #return second_month

        if now > second_month:
            return "Expired"
        else:
            return "Active"
    else:
        return "N/A"

    #last_record = Record.objects.get(issue=last_issue)
    
    #if now > first_month:
    #    return False
    #else:
    #    return True
    #return last_issue
   




    