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
        #season will attach to issue middle month (jan, mar, jun, or sep)
        issue_19 = datetime.date(2016, 10, 1)  # issue 19 is oct 2016
        months = (last_issue-19)*3 + 1
        issue_delta = relativedelta(months=months)
        last_month = issue_19 + issue_delta #date object

        #expiration flips to expire at the first day of the last month of each quarterly pub

        if now > last_month:
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
   




    