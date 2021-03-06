from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse

from cart.models import Cart, CartItem
from catalog.models import Subscription
from articles.models import Issue
from customers.models import Recipient
from catalog.views import issue_date
from orders.models import Record

# Create your views here.


def calc_cart_shipping_total(cart):
    cart = Cart.objects.get(id=cart)
    singles = CartItem.single_type.filter(cart=cart)
    new_total_shipping_qty = 0
    for item in singles:
        new_total_shipping_qty += item.quantity
    if new_total_shipping_qty > 0:
        cart.shipping_total = round((new_total_shipping_qty * 0.7829 + 4.6591), 1)
    else:
        cart.shipping_total = 0
    cart.save()


def calc_cart_total(request, cart):
    cart = Cart.objects.get(id=cart)
    new_subtotal = 0
    new_total = 0
    cart_qty_count = 0
    for item in cart.cartitem_set.all():
        new_subtotal += item.line_total
        cart_qty_count += item.quantity

    cart.product_total = new_subtotal
    cart.total = cart.product_total + cart.shipping_total
    print cart_qty_count
    request.session['items_total'] = cart_qty_count
    cart.save()


def view_cart(request):
    try:
        the_cart_id = request.session['cart_id']
    except:
        the_cart_id = None
    if the_cart_id:
        cart = Cart.objects.get(id=the_cart_id)
        subbies = CartItem.subbie_type.filter(cart=cart)
        singles = CartItem.single_type.filter(cart=cart)

        context = {"cart": cart, "subbies": subbies, "singles": singles}
    else:
        empty_message = 'Your Cart is currently empty. '
        context = {"empty": True, "empty_message": empty_message}
    # print request.session['items_total']

    template = "cart/cart.html"
    return render(request, template, context)


def remove_from_cart(request, slug):
    request.session.set_expiry(3000)
    #qty = request.POST['qty']

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("view_cart"))

    cart_item_to_go = CartItem.objects.filter(cart=cart, flug=slug)[:1].values_list("id", flat=True)
    CartItem.objects.filter(pk__in=list(cart_item_to_go)).delete()

    calc_cart_shipping_total(cart.id)

    calc_cart_total(request, cart.id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def increment_cart(request, slug):
    request.session.set_expiry(3000)

    try:
        the_id = request.session['cart_id']
    except:
        return HttpResponseRedirect(reverse("view_cart"))

    cart = Cart.objects.get(id=the_id)
    cart_item = CartItem.objects.get(cart=cart, flug=slug)
    piece_price = cart_item.line_total / cart_item.quantity
    cart_item.quantity += 1
    cart_item.line_total = cart_item.quantity * piece_price
    cart_item.save()

    calc_cart_shipping_total(cart.id)

    calc_cart_total(request, cart.id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def decrement_cart(request, slug):
    request.session.set_expiry(3000)

    try:
        the_id = request.session['cart_id']
    except:
        return HttpResponseRedirect(reverse("view_cart"))

    cart = Cart.objects.get(id=the_id)
    cart_item = CartItem.objects.get(cart=cart, flug=slug)
    piece_price = cart_item.line_total / cart_item.quantity
    cart_item.quantity += -1
    cart_item.line_total = cart_item.quantity * piece_price
    if cart_item.quantity == 0:
        cart_item.delete()
    else:
        cart_item.save()

    calc_cart_shipping_total(cart.id)

    calc_cart_total(request, cart.id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update_cart(request, slug):
    request.session.set_expiry(3000)
    #qty = request.POST['qty']

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    subscription = Subscription.objects.get(slug=slug)
    cart_item = CartItem.objects.create(cart=cart, subscription=subscription, flug=slug)
    cart_item.line_total = subscription.price
    print "line total is %s " % cart_item.line_total
    cart_item.save()

    calc_cart_shipping_total(cart.id)

    calc_cart_total(request, cart.id)

    return HttpResponseRedirect(reverse("view_cart"))


def add_subscribe_again_to_cart(request, recipient_id):
    request.session.set_expiry(3000)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    if request.method == "POST":
        #qty = request.POST['qty']
        print "we got post add to cart"
        try:
            print "we got post and add subscribe again to card"
            subscription = Subscription.objects.filter(is_active=1).filter(type=1).first()
            print subscription
            flug = subscription.slug
            recipient = Recipient.objects.get(id=recipient_id)
            print flug
            print recipient
            cart_item = CartItem.objects.create(cart=cart, subscription=subscription, flug=flug, recipient=recipient)
            cart_item.line_total = subscription.price
            print "line total is %s " % cart_item.line_total
            cart_item.save()
        except:
            pass
    else:
        pass

    
    calc_cart_shipping_total(cart.id)

    calc_cart_total(request, cart.id)
    # success message
    request.session['items_total'] = cart.cartitem_set.count()

    return HttpResponseRedirect(reverse("view_cart"))    



def add_to_cart(request, slug):
    request.session.set_expiry(3000)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    if request.method == "POST":
        #qty = request.POST['qty']
        print "we got post add to cart"
        try:
            print "we got post and add subscription"
            subscription = Subscription.objects.get(slug=slug)
            cart_item = CartItem.objects.create(cart=cart, subscription=subscription, flug=slug)
            cart_item.line_total = subscription.price
            print "line total is %s " % cart_item.line_total
            cart_item.save()

        except Subscription.DoesNotExist:
            print "no sub exists, so this is a single issue"
            issue = Issue.objects.get(slug=slug)
            #cart_item = CartItem.objects.create(cart=cart, single=issue, flug=slug)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, single=issue, flug=slug)
            if created:
                print "single issue cart item created"
                qty = 1
                cart_item.quantity = qty
                cart_item.line_total = issue.price
                cart_item.save()

                print "line total is %s " % cart_item.line_total
            else:
                print "single issue cart item found"
                qty = cart_item.quantity
                print qty
                new_qty = qty + 1
                cart_item.quantity = new_qty
                print cart_item.quantity
                cart_item.line_total = issue.price * new_qty
                cart_item.save()

                print "line total is %s " % cart_item.line_total

        except:
            print "other"
            # error message
            return HttpResponseRedirect(reverse("view_cart"))

        calc_cart_shipping_total(cart.id)

        calc_cart_total(request, cart.id)
        # success message
        request.session['items_total'] = cart.cartitem_set.count()
        return HttpResponseRedirect(reverse("view_cart"))

    return HttpResponseRedirect(reverse("view_cart"))


def add_renewal_to_cart(request, slug, recipient_id):
    request.session.set_expiry(3000)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    if request.method == "POST":
        print "we got post add renewal to cart"
        try:
            print "we got post and add renewal"
            subscription = Subscription.objects.get(slug=slug)
            print subscription
            recipient = Recipient.objects.get(id=recipient_id)
            print recipient
            # check if renewal item of same recip is in cart already
            items = CartItem.objects.filter(cart=cart)
            print items
            for item in items:
                
                if recipient == item.recipient and item.subscription:
                    print "already in cart!"
                    messages.error(request, 
                                    "This renewal is already in your cart. <a href='/cart/'>View Cart</a>",
                                    extra_tags='safe')
                    return HttpResponseRedirect(reverse("dashboard"))
                else:
                    pass


            cart_item = CartItem.objects.create(cart=cart, subscription=subscription, flug=slug, recipient=recipient)
            print cart_item
            cart_item.line_total = subscription.price
            print "line total is %s " % cart_item.line_total
            last_record = Record.objects.filter(recipient=recipient).order_by('issue').last()
            begin_issue = last_record.issue + 1
            print "first issue is %s" % begin_issue
            cart_item.begin_date = issue_date(begin_issue)
            cart_item.save()

        except:
            print "other"
            # error message
            return HttpResponseRedirect(reverse("view_cart"))

        calc_cart_shipping_total(cart.id)

        calc_cart_total(request, cart.id)
        # success message
        request.session['items_total'] = cart.cartitem_set.count()
        return HttpResponseRedirect(reverse("view_cart"))

    return HttpResponseRedirect(reverse("view_cart"))


def delete(request):
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

    return HttpResponseRedirect(reverse("view_cart"))
