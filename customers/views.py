from django.shortcuts import render, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from django.utils.html import strip_tags
import json
from django.contrib.auth import get_user_model
User = get_user_model()

from customers.forms import RecipientAddressForm
from customers.models import Recipient
from cart.models import CartItem, Cart
from orders.models import Order
from django.contrib import messages

# Create your views here.


def add_existing_recipient(request):

    if request.method == 'POST':
        print "existing add view"
        print request.POST
        id = request.POST.get("recipOption", "")
        recipient = Recipient.objects.get(id=id)
        print recipient
        # check if recipient is one of the users
        # if recipient.user != request.user:
        # bye
        #     return HttpResponseRedirect(reverse("checkout")
        # else:
        try:
            next = request.POST.get("next")
        except:
            next = None
        print "next is %s" % next

        try:
            itm = request.POST.get("itm")
        except:
            itm = None
        print "itm is %s" % itm

        try:
            rec = request.POST.get("rec")
        except:
            rec = None
        print "rec is %s" % rec

        if itm != "None":
            # subbie
            print "were getting cart itme with itm"
            ci = CartItem.objects.get(id=itm)
            ci.recipient = recipient
            ci.save()

        if rec != "None":
            # single, order main recip
            print "were getting oder with rec"
            order = Order.objects.get(id=rec)
            order.main_recipient = recipient
            order.save()

        return HttpResponseRedirect(reverse("checkout"))
    else:
        return HttpResponseRedirect(reverse("checkout"))

def is_this_my_recipient(recipient_id, user_id):
    """check if this is my recipient, so i cannot edit someone else's"""
    recipient = Recipient.objects.get(id=recipient_id)
    user = User.objects.get(id=user_id)
    my_recipients = Recipient.objects.filter(user=user)
    if my_recipients.filter(pk=recipient.pk).count():
        return True     
    else:
        return False
        


def edit_recipient(request):
    next = request.GET.get("next", "")
    rec = request.GET.get("rec", "")
    submit_btn = "Save"
    form_title = "Edit Recipient"
    recipient = Recipient.objects.get(id=rec)

    #safety first
    if is_this_my_recipient(recipient.id, request.user.id):
        pass # yep, this is my recipient
    else:
        return HttpResponseRedirect(reverse("dashboard")) #gtfo

    recipient_form = RecipientAddressForm(instance=recipient)

    if request.method == "POST":
        recipient_form = RecipientAddressForm(request.POST, instance=recipient)
        
        print "edit form posted"
        print request.POST
        if recipient_form.is_valid(): 

            print "edit form valid"
            #new_address = recipient_form.save(commit=False)
            #new_address.user = request.user

            #new_address.recipient = str(cart_item)
            #new_address.save()
            recipient_form.save()
            print "did it save?"

            if next is not None:
                return HttpResponseRedirect(reverse(str(next)))
        else:
           print recipient_form.errors #To see the form errors in the console. 


    context = {"recipient_form": recipient_form,
               "submit_btn": submit_btn,
               "form_title": form_title,
               "rec": rec,
               "next": next,
               }

    template = "customers/add_recipient.html"
    return render(request, template, context)


def add_recipient(request):
    print request.GET
    try:
        next = request.GET.get("next")
    except:
        next = None

    try:
        itm = request.GET.get("itm")
        ci = CartItem.objects.get(id=itm)
        cart = ci.cart
        all_cartitems = cart.cartitem_set.all()
        busy_recips = []
        for ci in all_cartitems:
            if ci.subscription:
                if ci.subscription.type == 2:
                    busy_recips.append(ci.recipient)
                else:
                    pass
        busy_ids = [bi.id for bi in busy_recips]

    except:
        itm = None
        busy_ids = None

    try:
        rec = request.GET.get("rec")
    except:
        rec = None

    # add context of existing recipients
    user = request.user
    if user.is_authenticated():
        pass
        recip_list = Recipient.objects.filter(user=user)
        if busy_ids:
            recip_list = recip_list.exclude(id__in=busy_ids)

    else:
        recip_list = None

    recipient_form = RecipientAddressForm(request.POST or None)
    if request.method == "POST":
        if recipient_form.is_valid():
            new_address = recipient_form.save(commit=False)
            #new_address.user = request.user

            #new_address.recipient = str(cart_item)
            new_address.save()

            if itm is not None:
                ci = CartItem.objects.get(id=itm)
                cart = ci.cart
                print "the cart is"
                print cart
                print ci
                ci.recipient = new_address
                print ci.recipient
                ci.save()

                if request.user.is_authenticated():
                    new_address.user = request.user
                    new_address.save()
                else:
                    pass
            if rec is not None:
                print rec
                order = Order.objects.get(id=rec)
                order.main_recipient = new_address
                order.save()
                print order
                if request.user.is_authenticated():
                    new_address.user = request.user
                    new_address.save()
                else:
                    pass
            # is_default = form.cleaned_data["default"]
            # if is_default:
            #     default_address, created = UserDefaultAddress.objects.get_or_create(user=request.user)
            #     default_address.shipping = new_address
            #     default_address.save()

            if next is not None:
                return HttpResponseRedirect(reverse(str(next)))

    submit_btn = "Add this Recipient"
    form_title = "Add New Address"

    context = {"recipient_form": recipient_form,
               "submit_btn": submit_btn,
               "form_title": form_title,
               "recip_list": recip_list,
               "itm": itm,
               "rec": rec,
               "next": next,
               }

    template = "customers/add_recipient.html"
    return render(request, template, context)


def delete_recipient(request, pk):
    recipient = Recipient.objects.get(pk=pk)
    recipient.delete()
    messages.success(request, "Successfully Removed Client.")
    return HttpResponseRedirect(reverse("dashboard"))


def purchase_notify(email_context, recipient):

    c = Context(email_context)
    sender = settings.DEFAULT_FROM_EMAIL
    recipients = [recipient, ]
    template = get_template('orders/purchase_notify_email.html')
    headers = {
        "X-SMTPAPI": json.dumps({
            "unique_args": {
                "campaign_id": 999
            },
            "category": "notice"
        })
    }

    subject = "Your Receipt"
    html_part = template.render(c)

    text_part = strip_tags(html_part)

    msg = EmailMultiAlternatives(subject, text_part, sender, recipients, headers=headers)
    msg.attach_alternative(html_part, "text/html")
    print "purchase nofication sent"
    return msg.send(True)
