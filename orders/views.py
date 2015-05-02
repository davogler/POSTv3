from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from orders.forms import OrderForm, PayForm
from cart.models import Cart, CartItem
from orders.models import Order
from orders.utils import id_generator
import stripe

# Create your views here.


def payout(request, order_id):
    pay_form = PayForm()
    order = Order.objects.get(order_id=order_id)
    cus = Customer.objects.get(id=order.customer.id)

    if request.POST:
        pay_form = PayForm(request.POST)
        token = request.POST['stripeToken']
        last4 = request.POST['last4']
        card_type = request.POST['card_type']
        # payer_name = request.POST['name']
        # payer_email = request.POST['email']

        if pay_form.is_valid():
            amount = int(order.total * 100)  # convert to cents
            fee = int(order.total * 100 * settings.TRINITY_FEE * .01)  # % of inputed ($) amount, in cents
            print fee
            return HttpResponseRedirect(reverse("view_cart"))
            try:
                customer = stripe.Customer.create(
                    card=token,
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
                # order.payer = payer_name
                # order.payer_email = payer_email
                order.last4 = last4
                order.card_type = card_type
                order.save()

                cus.stripe_id = customer.id
                cus.save()

                # # email notice
                # student_email = cus.email
                # payer_email = order.payer_email
                # order_id = order.order_id
                # cart = order.cart
                # items = CartItem.objects.filter(cart=cart)

                # email_context = {
                #     "order": order,
                #     "customer": cus,
                #     "items": items,
                # }
                # if settings.EMAIL_NOTIFICATIONS == True:
                #     notify(email_context, student_email, payer_email, order_id)
                # else:
                #     pass

                order_id = order.order_id
                try:
                    the_cart_id = request.session['cart']
                    cart = Cart.objects.get(id=the_cart_id)
                except:
                    cart = False
                if cart:
                    deactivate = Cart.objects.get(id=the_cart_id)
                    deactivate.active = False
                    deactivate.save()
                    del request.session['cart']
                    del request.session['items_total']

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
                # Authentication with Stripe's API failed
                # (maybe you changed API keys recently)
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except stripe.error.APIConnectionError, e:
                # Network communication with Stripe failed
                messages.error(request, "%s The payment could not be completed." % err['message'])
            except stripe.error.StripeError, e:
                # Display a very generic error to the user, and maybe send
                messages.error(request, "%s The payment could not be completed." % err['message'])
                # yourself an email
            except Exception, e:
                # Something else happened, completely unrelated to Stripe
                messages.error(request, "Something bizzare happened. The payment could not be completed." )
                

    context = {
        "pay_form": pay_form,
        "order": order,
    }
    template = "orders/payout.html"
    return render(request, template, context)


def checkout(request):
    try:

        the_cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_cart_id)
        print "we have a cart"
        subbies = CartItem.subbie_type.filter(cart=cart)
        singles = CartItem.single_type.filter(cart=cart)
        cart_items = CartItem.objects.filter(cart=cart)

        print "subbies - %s" % subbies
        print "singles - %s" % singles

    except:

        the_cart_id = None
        print "we have no cart"
        return HttpResponseRedirect(reverse("view_cart"))
    try:
        user = request.user
    except:
        user = None
    print "user is %s" % user
    try:

        new_order = Order.objects.get(cart=cart)
        print "we got an order that exists"
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        
        
        new_order.order_id = id_generator()
        new_order.save()
        print "we made a new order and saved it"
    except:
        new_order = None
        # work on some error message
        print "narnia"
        return HttpResponseRedirect(reverse("view_cart"))

    if request.user.is_authenticated():
            print "is"
            new_order.user = request.user
    new_order.total = cart.total
    new_order.save()
    pay_form = PayForm()
    order = new_order
    print "the order is %s" % order.order_id

    if request.POST:
        pay_form = PayForm(request.POST)
        token = request.POST['stripeToken']
        last4 = request.POST['last4']
        card_type = request.POST['card_type']
        print request.POST
        payer_name = request.POST['name']
        payer_email = request.POST['email']

        if pay_form.is_valid():
            amount = int(order.total * 100)  # convert to cents
            fee = int(order.total * 100 * settings.TRINITY_FEE * .01)  # % of inputed ($) amount, in cents
            print fee
            
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
                # order.payer = payer_name
                # order.payer_email = payer_email
                order.last4 = last4
                order.card_type = card_type
                order.save()

                # cus.stripe_id = customer.id
                # cus.save()

                # # email notice
                # student_email = cus.email
                # payer_email = order.payer_email
                # order_id = order.order_id
                # cart = order.cart
                # items = CartItem.objects.filter(cart=cart)

                # email_context = {
                #     "order": order,
                #     "customer": cus,
                #     "items": items,
                # }
                # if settings.EMAIL_NOTIFICATIONS == True:
                #     notify(email_context, student_email, payer_email, order_id)
                # else:
                #     pass

                order_id = order.order_id
                try:
                    the_cart_id = request.session['cart']
                    cart = Cart.objects.get(id=the_cart_id)
                except:
                    cart = False
                if cart:
                    deactivate = Cart.objects.get(id=the_cart_id)
                    deactivate.active = False
                    deactivate.save()
                    del request.session['cart']
                    del request.session['items_total']

                return HttpResponseRedirect(reverse('result', args=(order_id,)))

            except stripe.CardError, e:
               pass
               

    context = {
        "order": new_order,
        "pay_form": pay_form,
        "subbies": subbies,
        "singles": singles,
        "cart_items": cart_items,
        "cart": cart,

    }
    template = "orders/checkout.html"
    return render(request, template, context)


def result(request, order_id):
    order = Order.objects.get(order_id=order_id)
    

    context = {
        "order": order,
        
    }
    template = "orders/result.html"
    return render(request, template, context)
