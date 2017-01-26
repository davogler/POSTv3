from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.generic import ListView, DetailView
from orders.utils import id_generator
from django.contrib import messages
import stripe
from django.template import Context
from django.utils.html import strip_tags
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site

from orders.forms import PayForm
from cart.models import Cart, CartItem
from customers.models import CreditCard, Recipient
from orders.models import Order, Record, BackIssue, Coupon
from customers.views import purchase_notify
from catalog.templatetags.catalog_tags import get_latest_issue


# Create your views here.

def accept_coupon(request):
    if request.POST:
        code = request.POST.get("couponCode", "")
        order_id = request.POST.get("orderID", "")
        print "accepting_coupn"
        print code, order_id
        if code and order_id:
            try:
                coupon = Coupon.objects.get(code=code)
                print coupon
                percent_discount = coupon.percent_discount
                print percent_discount

                order = Order.objects.get(order_id=order_id)
                print order
                # new_total = order.total - order.total * (float(percent_discount) / 100)
                # order.total = new_total
                # print new_total
                order.coupon = coupon
                order.save()
                print "made it"
                return HttpResponseRedirect(reverse("checkout"))



            except:
                coupon = None
                print "exception"
                return HttpResponseRedirect(reverse("checkout"))
        

    else:
        return HttpResponseRedirect(reverse("checkout"))



def renewals_get(request):
    # prepare default
    latest_issue = get_latest_issue()
    latest_issue_number = latest_issue.first_issue
    issue = request.GET.get('issue', latest_issue_number)
    # if not a number, just make it latest issue
    try:
        int(issue)
    except:
        issue = latest_issue_number
    # go to renewals with this issue number
    return HttpResponseRedirect(reverse('renewals', args=(issue,)))


def renewals(request, issue):
    expiring_issue = int(issue) - 1

    # get all recipients of the next issue and make a list.
    upcoming_issue_records = Record.objects.filter(issue=issue)
    upcoming_issue_recipients = set()
    for record in upcoming_issue_records:
        upcoming_issue_recipients.add(record.recipient)
    # prefetch orders and carts to go with every record that is expiring.
    # exclude those who are on the above list for the next issue -  remaining are the expiring records
    expiring_records = Record.objects.filter(issue=expiring_issue).exclude(
        recipient__in=upcoming_issue_recipients).prefetch_related('originating_order__cart')

    # # here is list of carts from the expiring recrods
    # cart_set = set()
    # for e in expiring_records:
    #     cart_set.add(e.originating_order.cart)

    # # here is a list of cart items in the carts of the orders that originated an expiring record.
    # item_set = set()
    # for cart in cart_set:
    #     print cart
    #     cart_items = CartItem.objects.filter(cart=cart)
    #     print cart_items
    #     for item in cart_items:
    #         if item.subscription:
    #             item_set.add(item)
    context = {
        "issue": issue,
        "expiring_issue": expiring_issue,
        "expiring_records": expiring_records,
    }
    template = "orders/renewals.html"
    return render(request, template, context)


def toggle_renew(request, item_id):
    if request.POST:
        print "post in toggle renew"

        print request.POST
        # c = request.POST['autoRenew']
        c = request.POST.get("autoRenew", "")
        cart_item = CartItem.objects.get(id=item_id)
        print "current autoRenew is %s " % cart_item.auto_renew
        if c == "on":
            print "autoRenew on was picked"
            cart_item.auto_renew = True
        else:
            print "autoRenew on was NOT picked"
            cart_item.auto_renew = False

        cart_item.save()
    print c
    return HttpResponseRedirect(reverse("checkout"))


def promos(request):
    promo_pool = Recipient.objects.filter(type = "Promo")
    staff_pool = Recipient.objects.filter(type = "Staff")

    context = {
        "promo_pool": promo_pool,
        "staff_pool": staff_pool,
    }
    template = "orders/promos.html"
    return render(request, template, context)


def notify_purchase(email_context, payer_email, order_id):
    c = Context(email_context)
    sender = settings.DEFAULT_FROM_EMAIL
    circulation_admin = settings.CIRCULATION_ADMIN

    template = get_template('orders/notify_purchase_email.html')
    recipients = [payer_email, circulation_admin]
    subject = "Confirming Order #%s at POST" % order_id
    html_part = template.render(c)
    text_part = strip_tags(html_part)

    msg = EmailMultiAlternatives(subject, text_part, sender, recipients, bcc=None)
    msg.attach_alternative(html_part, "text/html")
    msg.send()

    return msg.send(True)

def add_credit_card(request):
    pay_form = PayForm()
    if request.user.is_authenticated():
        user=request.user
    else:
        return HttpResponseRedirect(reverse("home"))
    if request.POST:
        print request.POST
        pay_form = PayForm(request.POST)
        token = request.POST['stripeToken']
        last4 = request.POST['last4']
        card_type = request.POST['card_type']
        payer_name = request.POST['name']
        payer_email = request.user

        if pay_form.is_valid():
            
            try:
                customer = stripe.Customer.create(
                    source=token,
                    description=payer_email,
                    api_key=settings.TRINITY_API_KEY,
                )

                if request.user.is_authenticated():
                    try:
                        # see if any other cc exist, and un default them
                        credit_cards = CreditCard.objects.filter(user=user)
                        for card in credit_cards:
                            card.default = False
                            card.save()
                    except:
                        pass
                    cc = CreditCard(user=user, last4=last4, card_type=card_type)
                    cc.stripe_id = customer.id
                    cc.payer_name = payer_name
                    cc.payer_email = payer_email
                    cc.save()

                else:
                    print "no user at hand"
                    pass
            except stripe.CardError, e:

                # Since it's a decline, stripe.error.CardError will be caught
                body = e.json_body
                err = body['error']

                print "Status is: %s" % e.http_status
                print "Type is: %s" % err['type']
                print "Code is: %s" % err['code']

                print "Message is: %s" % err['message']
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except stripe.error.InvalidRequestError, e:
                # Invalid parameters were supplied to Stripe's API
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except stripe.error.AuthenticationError, e:
                # Authentication with Stripe's API failed (maybe you changed API keys recently)
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except stripe.error.APIConnectionError, e:
                # Network communication with Stripe failed
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except stripe.error.StripeError, e:
                # Display a very generic error to the user, and maybe send yourself an email
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except Exception, e:
                # Something else happened, completely unrelated to Stripe
                messages.error(request, "Something bizzare happened. The payment could not be completed.")

        messages.success(request, "You successfully added a credit card!")
        return HttpResponseRedirect(reverse("dashboard"))


    context = {
       
        "pay_form": pay_form,
   

    }
    template = "orders/add_credit_card.html"
    return render(request, template, context)



    


def checkout_saved_cc(request):
    try:
        the_cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_cart_id)
        subbies = CartItem.subbie_type.filter(cart=cart)
        singles = CartItem.single_type.filter(cart=cart)
        cart_items = CartItem.objects.filter(cart=cart)
        cc_id = request.POST['ccRadios']
        cc = CreditCard.objects.get(id=cc_id)
    except:
        the_cart_id = None
        return HttpResponseRedirect(reverse("view_cart"))
    try:
        user = request.user
    except:
        user = None

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.order_id = id_generator()
        new_order.save()
    except:
        new_order = None
        return HttpResponseRedirect(reverse("view_cart"))

    if request.POST:
        order = new_order
        amount = int(order.total * 100)  # convert to cents
        fee = int(order.total * 100 * settings.TRINITY_FEE * .01)  # % of inputed ($) amount, in cents
        customer = cc.stripe_id
        try:
            charge = stripe.Charge.create(
                amount=amount,  # amount in cents, again
                currency="usd",
                application_fee=fee,
                customer=customer,
                api_key=settings.TRINITY_API_KEY,
            )

            order.status = "Finished"
            order.payer_name = cc.payer_name
            order.payer_email = cc.payer_email
            order.last4 = cc.last4
            order.card_type = cc.card_type
            order.save()

            order_id = order.order_id
            # make records here:
            # get recipient, check for last record. is last record greater than sub. first issue?
            # first look for latest record for this recipient, if greater than subscription.first_issue

            print "HERE in checkout-cc, we are going to make recrods"

            print "order is %s" % order
            print "cart is %s" % cart
            print "cart items is %s" % cart_items
            print "subbies is %s" % subbies
            print "singlges is %s" % singles

            for sub in subbies:
                # two paths here- regular subbie and renewal
                print "wea are in subbie path"
                recipient = sub.recipient
                print recipient
                print "type is %s" % sub.subscription.type
                if sub.subscription.type == 2:  # renewal
                    print "chcekout cc, renewal"
                    last_record = Record.objects.filter(recipient=recipient).order_by('issue').last()
                    ish = last_record.issue + 1
                else:  # not renewal
                    print "checkout cc not renewal"
                    ish = sub.subscription.first_issue

                # try:
                #    all_record = Record.objects.get(recipient=sub.recipient, originating_order=order, issue=ish)

                for x in range(0, sub.subscription.term):
                    try:
                        record = Record.objects.get(recipient=sub.recipient, originating_order=order, issue=ish)
                        pass
                    except Record.DoesNotExist:
                        new_record = Record(recipient=sub.recipient, originating_order=order, issue=ish)
                        new_record.save()
                    ish += 1

            for single in singles:
                ish = int(single.single.slug)
                print "cehkout cc single"
                try:
                    bo = BackIssue.objects.get(
                        recipient=order.main_recipient, originating_order=order, issue=ish, quantity=single.quantity)
                    pass
                except BackIssue.DoesNotExist:
                    new_bo = BackIssue(
                        recipient=order.main_recipient, originating_order=order, issue=ish, quantity=single.quantity)
                    new_bo.save()

            order.status = "Recorded"
            order.save()

            try:
                the_cart_id = request.session['cart_id']
                cart = Cart.objects.get(id=the_cart_id)
            except:
                cart = False
            if cart:
                deactivate = Cart.objects.get(id=the_cart_id)
                deactivate.active = False
                deactivate.save()
                del request.session['cart_id']
                del request.session['items_total']

            # now we notify.
            current_site = Site.objects.get_current()
            local = settings.LOCAL
            email_context = {
                "cart": cart,
                "subbies": subbies,
                "singles": singles,
                "order": order,
                "cart_items": cart_items,
                "current_site": current_site,
                "local": local,
            }

            if settings.EMAIL_NOTIFICATIONS is True:
                recipient = "david.vogler@kekdesign.com"
                print "email notifications are true and we're about to send"

                purchase_notify(email_context, recipient)

            else:
                print "email settings not true"
                pass

            return HttpResponseRedirect(reverse('result', args=(order_id,)))

        except stripe.CardError, e:

            # Since it's a decline, stripe.error.CardError will be caught
            body = e.json_body
            err = body['error']

            print "Status is: %s" % e.http_status
            print "Type is: %s" % err['type']
            print "Code is: %s" % err['code']

            print "Message is: %s" % err['message']
            messages.error(request, "%s The payment could not be completed." % err['message'])
        except stripe.error.InvalidRequestError, e:
            # Invalid parameters were supplied to Stripe's API
            messages.error(request, "%s The payment could not be completed." % err['message'])
        except stripe.error.AuthenticationError, e:
            # Authentication with Stripe's API failed (maybe you changed API keys recently)
            messages.error(request, "%s The payment could not be completed." % err['message'])
        except stripe.error.APIConnectionError, e:
            # Network communication with Stripe failed
            messages.error(request, "%s The payment could not be completed." % err['message'])
        except stripe.error.StripeError, e:
            # Display a very generic error to the user, and maybe send yourself an email
            messages.error(request, "%s The payment could not be completed." % err['message'])
        except Exception, e:
            # Something else happened, completely unrelated to Stripe
            messages.error(request, "Something bizzare happened. The payment could not be completed.")

    return HttpResponseRedirect(reverse("dashboard"))


def checkout(request):
    try:
        the_cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_cart_id)
        subbies = CartItem.subbie_type.filter(cart=cart)
        singles = CartItem.single_type.filter(cart=cart)
        cart_items = CartItem.objects.filter(cart=cart)

    except:
        the_cart_id = None
        return HttpResponseRedirect(reverse("view_cart"))

    try:
        user = request.user
    except:
        user = None

    try:

        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.order_id = id_generator()
        new_order.save()
    except:
        new_order = None
        return HttpResponseRedirect(reverse("view_cart"))

    if request.user.is_authenticated():
        new_order.user = request.user
        print new_order.user
        print "we gota  new order user"

    new_order.total = cart.total
    new_order.shipping = cart.shipping_total
    if new_order.coupon:
        coupon = new_order.coupon
        percent_discount = coupon.percent_discount
        new_total = new_order.total - new_order.total * (float(percent_discount) / 100)
        print new_total
        new_order.total = new_total
    new_order.save()
    pay_form = PayForm()
    order = new_order

    subgo = False
    singo = False
    paygo = False
    usergo = False

    if subbies and singles:
        for sub in subbies:
            if sub.recipient:
                subgo = True
            else:
                subgo = False
        if order.main_recipient:
            singo = True
        else:
            singo = False

        if subgo == True and singo == True:
            paygo = True
        else:
            paygo = False

    elif not subbies and singles:
        if order.main_recipient:
            singo = True
        else:
            singo = False

        if subgo == False and singo == True:
            paygo = True
        else:
            paygo = False

    elif subbies and not singles:
        for sub in subbies:
            if sub.recipient:
                subgo = True
            else:
                subgo = False

        if subgo == True and singo == False:
            paygo = True
        else:
            paygo = False

    # check user status
    user = request.user
    if user.is_authenticated():
        usergo = True
    elif singles and not subbies:
        usergo = True
    else:
        usergo = False

    if request.POST:
        pay_form = PayForm(request.POST)
        token = request.POST['stripeToken']
        last4 = request.POST['last4']
        card_type = request.POST['card_type']
        payer_name = request.POST['name']
        payer_email = request.POST['email']

        if pay_form.is_valid():
            amount = int(order.total * 100)  # convert to cents
            fee = int(order.total * 100 * settings.TRINITY_FEE * .01)  # % of inputed ($) amount, in cents

            try:
                customer = stripe.Customer.create(
                    source=token,
                    description=payer_email,
                    api_key=settings.TRINITY_API_KEY,
                )

                charge = stripe.Charge.create(
                    amount=amount,  # amount in cents, again
                    currency="usd",
                    application_fee=fee,
                    customer=customer.id,
                    api_key=settings.TRINITY_API_KEY,
                )

                order.status = "Finished"
                order.payer_name = payer_name
                order.payer_email = payer_email
                order.last4 = last4
                order.card_type = card_type
                order.save()

                if request.user.is_authenticated():
                    try:
                        # see if any other cc exist, and un default them
                        credit_cards = CreditCard.objects.filter(user=user)
                        for card in credit_cards:
                            card.default = False
                            card.save()
                    except:
                        pass
                    cc = CreditCard(user=user, last4=last4, card_type=card_type)
                    cc.stripe_id = customer.id
                    cc.payer_name = payer_name
                    cc.payer_email = payer_email
                    cc.save()

                else:
                    print "no user at hand"
                    pass

                order_id = order.order_id
                # make records here:
                # get recipient, check for last record. is last record greater than sub. first issue?
                # first look for latest record for this recipient, if greater than subscription.first_issue
                for sub in subbies:
                    # two paths here- regular subbie and renewal
                    recipient = sub.recipient
                    print recipient
                    if sub.subscription.type == 2:  # renewal

                        last_record = Record.objects.filter(recipient=recipient).order_by('issue').last()
                        ish = last_record.issue + 1
                    else:
                        ish = sub.subscription.first_issue

                    # try:
                    #    all_record = Record.objects.get(recipient=sub.recipient, originating_order=order, issue=ish)

                    for x in range(0, sub.subscription.term):
                        try:
                            record = Record.objects.get(recipient=sub.recipient, originating_order=order, issue=ish)
                            pass
                        except Record.DoesNotExist:
                            new_record = Record(recipient=sub.recipient, originating_order=order, issue=ish)
                            new_record.save()
                        ish += 1

                for single in singles:
                    ish = int(single.single.slug)
                    try:
                        bo = BackIssue.objects.get(
                            recipient=order.main_recipient, originating_order=order, issue=ish, quantity=single.quantity)
                        pass
                    except BackIssue.DoesNotExist:
                        new_bo = BackIssue(
                            recipient=order.main_recipient, originating_order=order, issue=ish, quantity=single.quantity)
                        new_bo.save()

                order.status = "Recorded"
                order.save()

                try:
                    the_cart_id = request.session['cart_id']
                    cart = Cart.objects.get(id=the_cart_id)
                except:
                    cart = False
                if cart:
                    deactivate = Cart.objects.get(id=the_cart_id)
                    deactivate.active = False
                    deactivate.save()
                    del request.session['cart_id']
                    del request.session['items_total']

                # now we notify.
                current_site = Site.objects.get_current()
                local = settings.LOCAL
                email_context = {
                    "cart": cart,
                    "subbies": subbies,
                    "singles": singles,
                    "order": order,
                    "cart_items": cart_items,
                    "current_site": current_site,
                    "local": local,
                }

                if settings.EMAIL_NOTIFICATIONS is True:
                    recipient = "david.vogler@kekdesign.com"
                    print "email notifications are true and we're about to send"

                    purchase_notify(email_context, recipient)

                else:
                    print "email settings not true"
                    pass

                return HttpResponseRedirect(reverse('result', args=(order_id,)))

            except stripe.CardError, e:

                # Since it's a decline, stripe.error.CardError will be caught
                body = e.json_body
                err = body['error']

                print "Status is: %s" % e.http_status
                print "Type is: %s" % err['type']
                print "Code is: %s" % err['code']

                print "Message is: %s" % err['message']
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except stripe.error.InvalidRequestError, e:
                # Invalid parameters were supplied to Stripe's API
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except stripe.error.AuthenticationError, e:
                # Authentication with Stripe's API failed (maybe you changed API keys recently)
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except stripe.error.APIConnectionError, e:
                # Network communication with Stripe failed
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except stripe.error.StripeError, e:
                # Display a very generic error to the user, and maybe send yourself an email
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except Exception, e:
                # Something else happened, completely unrelated to Stripe
                messages.error(request, "Something bizzare happened. The payment could not be completed.")

    context = {
        "order": new_order,
        "pay_form": pay_form,
        "subbies": subbies,
        "singles": singles,
        "cart_items": cart_items,
        "cart": cart,
        "paygo": paygo,
        "usergo": usergo,

    }
    template = "orders/checkout.html"
    return render(request, template, context)


def email_preview(request, order_id):
    current_site = Site.objects.get_current()
    local = settings.LOCAL
    order = Order.objects.get(order_id=order_id)
    the_cart_id = request.session['cart_id']
    cart = Cart.objects.get(id=the_cart_id)
    subbies = CartItem.subbie_type.filter(cart=cart)
    singles = CartItem.single_type.filter(cart=cart)
    cart_items = CartItem.objects.filter(cart=cart)
    context = {
        "cart": cart,
        "subbies": subbies,
        "singles": singles,
        "order": order,
        "cart_items": cart_items,
        "current_site": current_site,
        "local": local,
    }
    template = "orders/purchase_notify_email.html"
    return render(request, template, context)


def email(request, order_id):
    current_site = Site.objects.get_current()
    local = settings.LOCAL
    order = Order.objects.get(order_id=order_id)
    the_cart_id = request.session['cart_id']
    cart = Cart.objects.get(id=the_cart_id)
    subbies = CartItem.subbie_type.filter(cart=cart)
    singles = CartItem.single_type.filter(cart=cart)
    cart_items = CartItem.objects.filter(cart=cart)

    email_context = {
        "subbies": subbies,
        "singles": singles,
        "order": order,
        "cart_items": cart_items,
        "current_site": current_site,
        "local": local,
    }

    if settings.EMAIL_NOTIFICATIONS is True:
        recipient = "david.vogler@kekdesign.com"
        print "email notifications are true and we're about to send"

        purchase_notify(email_context, recipient)

    else:
        print "email settings not true"
        pass

    return HttpResponseRedirect(reverse("checkout"))


def result(request, order_id):
    order = Order.objects.get(order_id=order_id)

    context = {
        "order": order,

    }
    template = "orders/result.html"
    return render(request, template, context)


def order_list(request):
    orders = Order.objects.all()

    context = {"orders": orders}
    template = "orders/order_list.html"
    return render(request, template, context)


def order_detail(request, order_id):
    order = Order.objects.get(order_id=order_id)
    cart = order.cart
    items = CartItem.objects.filter(cart=cart)
    subbies = CartItem.subbie_type.filter(cart=cart)
    singles = CartItem.single_type.filter(cart=cart)

    context = {"order": order,
               "items": items,
               "subbies": subbies,
               "singles": singles,
               "cart": cart,
               }
    template = "orders/order_detail.html"
    return render(request, template, context)


def records_get(request):
    # prepare default
    latest_issue = get_latest_issue()
    latest_issue_number = latest_issue.first_issue
    issue = request.GET.get('issue', latest_issue_number)
    # if not a number, just make it latest issue
    try:
        int(issue)
    except:
        issue = latest_issue_number
    # go to renewals with this issue number
    return HttpResponseRedirect(reverse('records', args=(issue,)))


def records(request, issue):
    # get all recipients of the next issue and make a list.
    records = Record.objects.filter(issue=issue)

    context = {"records": records,
               "issue": issue,
               }
    template = "orders/record_list.html"
    return render(request, template, context)


def record_by_issue(request, issue):
    records = Record.objects.filter(issue=issue)

    context = {"records": records, "issue": issue}
    template = "orders/record_by_issue.html"
    return render(request, template, context)

# view to turn order into record.


def order_record(request, order_id):
    order = Order.objects.get(order_id=order_id)
    cart = order.cart

    subbies = CartItem.subbie_type.filter(cart=cart)
    singles = CartItem.single_type.filter(cart=cart)

    for sub in subbies:
        ish = sub.subscription.first_issue
        for x in range(0, sub.subscription.term):
            try:
                record = Record.objects.get(recipient=sub.recipient, originating_order=order, issue=ish)
                pass
            except Record.DoesNotExist:
                new_record = Record(recipient=sub.recipient, originating_order=order, issue=ish)
                new_record.save()
            ish += 1

    for single in singles:
        print order.main_recipient
        print single.single.slug
        ish = int(single.single.slug)
        print single.quantity
        try:
            bo = BackIssue.objects.get(
                recipient=order.main_recipient, originating_order=order, issue=ish, quantity=single.quantity)
            pass
        except BackIssue.DoesNotExist:
            new_bo = BackIssue(
                recipient=order.main_recipient, originating_order=order, issue=ish, quantity=single.quantity)
            new_bo.save()

    order.status = "Recorded"
    order.save()
    return HttpResponseRedirect(reverse("order_detail", args=(order.order_id,)))
