from django.shortcuts import render, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.conf import settings
from customers.forms import RecipientAddressForm
from customers.models import Recipient
from cart.models import CartItem
from orders.models import Order

# Create your views here.


def add_recipient(request):
    print request.GET
    try:
        next_page = request.GET.get("next")
    except:
        next_page = None

    try:
        cart_item = request.GET.get("itm")
    except:
        cart_item = None
    print cart_item

    try:
        recip = request.GET.get("rec")
    except:
        recip = None
    print recip

    recipient_form = RecipientAddressForm(request.POST or None)
    if request.method == "POST":
        if recipient_form.is_valid():
            new_address = recipient_form.save(commit=False)
            #new_address.user = request.user


            #new_address.recipient = str(cart_item)
            new_address.save()

            if cart_item is not None:
                ci = CartItem.objects.get(id=cart_item)
                print ci
                ci.recipient = new_address
                print ci.recipient
                ci.save()
            if recip is not None:
                print recip
                order = Order.objects.get(id=recip)
                order.main_recipient = new_address
                order.save()
                print order
            # is_default = form.cleaned_data["default"]
            # if is_default:
            #     default_address, created = UserDefaultAddress.objects.get_or_create(user=request.user)
            #     default_address.shipping = new_address
            #     default_address.save()

            if next_page is not None:
                return HttpResponseRedirect(reverse(str(next_page)))
    
    submit_btn = "Save Address"
    form_title = "Add New Address"

    context = {"recipient_form": recipient_form,
                "submit_btn": submit_btn,
                "form_title": form_title,
             }

    template = "customers/add_recipient.html"
    return render(request, template, context)
    