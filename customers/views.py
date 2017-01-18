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
from customers.models import Recipient, CreditCard
from catalog.models import Subscription
from cart.models import CartItem, Cart
from orders.models import Order, Record
from django.contrib import messages

# Create your views here.


def add_existing_recipient(request):

    if request.method == 'POST':
        print "adding an existing recipient"
        print request.POST
        id = request.POST.get("recipOption", "")
        #get the recipient object
        recipient = Recipient.objects.get(id=id)
        print recipient

        try:
            next = request.POST.get("next")
        except:
            next = None
        print "next is %s" % next

        try:
            rec = request.POST.get("rec")
        except:
            rec = None
        print "rec is %s" % rec

        try:
            itm = request.POST.get("itm")
        except:
            # item is a single, not a subbie
            itm = None
        print "itm is %s" % itm

        if rec != "None":
            # single, order has main recip; assign.
            print "were getting order with a main recipient-a single"
            order = Order.objects.get(id=rec)
            order.main_recipient = recipient
            order.save()

        if itm != "None":
            # if itm exists, this item is a subbie, so get it and its cart
            print "we are getting cart item with itm = %s" % itm
            ci = CartItem.objects.get(id=itm)
            cart = Cart.objects.get(id=ci.cart.id)
        #     items = CartItem.objects.filter(cart=cart)
        #     print "here follows a list of items in the cart"
        #     print items
        #     for item in items:      
        #         print "item recipient is %s" % item.recipient
        #         print "item subscritpion is %s" % item.subscription
        #         # for each item, check if it has same recipient and if it is a subbie
        #         # get starting issue from subscription
        #         # subtract one to get last active issue
        #         starting_issue = item.subscription.first_issue
        #         last_issue = starting_issue -1 
        #         print "starting issue is %s" % starting_issue
        #         print "last issue is %s" % last_issue
        #         try: 
        #             # look for records with this recip and starting issue
        #             record = Record.objects.get(recipient=recipient, issue=starting_issue)
        #             print "we have a record, it is %s" % record
        #         except:
        #             record = None
        #             print "record retrieve excpetion"
                
        #         if recipient == item.recipient and item.subscription:
        #             print "changed address to active recipient!"

        #             messages.error(request,
        #                            "This recipient has an active subscription. \
        #                            This subscription will be added after the current subscription ends",
        #                            extra_tags='safe')
        #             return HttpResponseRedirect(reverse("checkout"))
        #         elif record != None and item.subscription:
        #             print "added an active recipient to a fresh unassigned subbie"
        #             # need to turn into a renewal
        #             # maybe bump to add_renewal url?
        #             renewal = Subscription.objects.get(slug="one-year-renewal")
        #             ci.subscription = renewal
        #             ci.save()
        #             messages.error(request,
        #                            "This recipient has an active subscription. \
        #                            New issues will be added after the current subscription ends",
        #                            extra_tags='safe')
        #             return HttpResponseRedirect(reverse("checkout"))
        #         else:
        #             print "did not detect recipient as active"
        #             return HttpResponseRedirect(reverse("checkout"))

        # # check if recipient is one of the users
        # # if recipient.user != request.user:
        # # bye
        # #     return HttpResponseRedirect(reverse("checkout")
        # # else:


        



        # this should go in sequence above when i figure it out
        if itm != "None":
            # this item is a subbie, assign new recip to it
            print "were getting cart item with itm = %s" % itm
            ci = CartItem.objects.get(id=itm)
            ci.recipient = recipient
            ci.save()



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
    next = request.GET.get("next", None)
    rec = request.GET.get("rec", None)
    itm = request.GET.get("itm", None)
    print next, rec, itm
    user = request.user
    if itm:
        print "we have subbie item"
        ci = CartItem.objects.get(id=itm)
        cart = ci.cart
        all_cartitems = cart.cartitem_set.all()
        incart_recipients = []
        for c in all_cartitems:
            if c.subscription and c.recipient:
                incart_recipients.append(c.recipient.id)
            else:
                pass
        
        first_issue = ci.subscription.first_issue if ci.subscription else None
        
        print "cart item is %s" % ci
        print "subscription is %s" % ci.subscription
        print "first issue is %s" % first_issue
        record_set = Record.objects.filter(issue=first_issue)
        print "record set %s" % record_set
        active_recipients = []
        for record in record_set:
            if record.recipient:
                active_recipients.append(record.recipient.id)
            else:
                pass
        print active_recipients


        
        

    else:
        print "we don't have subbie item"
        itm = None
        incart_recipients = None
        active_recipients = None


    
   

    # add context of existing recipients in cart
    
    if user.is_authenticated():
        recip_list = Recipient.objects.filter(user=user)
        
       

        
        if incart_recipients:
            # incart are recips that are already in the cart (renewal or new)
            recip_list = recip_list.exclude(id__in=incart_recipients)
            
        if active_recipients:
            # active are recips that already getting an issue (via record)
            recip_list = recip_list.exclude(id__in=active_recipients)

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

def delete_creditcard(request, pk):
    cc = CreditCard.objects.get(pk=pk)
    cc.delete()
    messages.success(request, "Successfully Removed Credit Card.")
    return HttpResponseRedirect(reverse("dashboard"))

