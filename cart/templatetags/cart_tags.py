from django.template import Library
from django import template
from django.db.models import get_model

from orders.models import Record

register = template.Library()


@register.assignment_tag
def get_last_record(recipient):
    try:
        last_record = Record.objects.filter(recipient = recipient).order_by('issue').last()
        if last_record != None:
            print "last record be %s " % last_record
        return int(last_record.issue + 1)
    except:
        print "last record is none"
        return None


@register.simple_tag
def get_larst_record(recipient, issue):
    return recipient

    # improve fetching last record to account for lapses

