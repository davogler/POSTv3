from django.template import Library
from django import template
from django.db.models import get_model

from orders.models import Record

register = template.Library()


@register.assignment_tag
def get_last_record(recipient):
    try:
        last_record = Record.objects.filter(recipient = recipient).order_by('issue').last()
        return last_record.issue + 1
    except:
        return None




