from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.views.generic import ListView, DetailView, TemplateView

from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()


from accounts.forms import LoginForm, SignupForm
from orders.models import Order
from cart.models import Cart, CartItem


# Create your views here.


def logout_view(request):
    print "logging out"
    logout(request)
    return HttpResponseRedirect('%s'%(reverse("auth_login")))

def login_view(request):
    form = LoginForm(request.POST or None)
    btn = "Login"
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        next = request.GET.get('next', '')
        messages.success(request, "Successfully Logged In. Welcome Back!")
        if next:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    context = {
        "form": form,
        "submit_btn": btn,
    }
    return render(request, "accounts/login-signup.html", context)


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        next = request.POST.get('next', '')

        # check for duplicate username/email
        try:
            user = User.objects.get(username=username)
            messages.error(request, "Whoops, this user exists already. Did you forget your password?")
            # whoops user exists
            return HttpResponseRedirect(reverse("signup"))
        except:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            

            user = authenticate(username=username, password=password)

            # don't log them in.
            login(request, user)
            next = request.GET.get('next', '')
            messages.success(request, "Thank you, you've successfully signed up for an account! You are now logged in")
            if next:
                
                # here is where signup happened mid-buy.  make sure recips get tagged with user.
                the_cart_id = request.session['cart_id']
                cart = Cart.objects.get(id=the_cart_id)
                print "we have a cart mid buy"
                subbies = CartItem.subbie_type.filter(cart=cart)
                order = Order.objects.get(cart=cart)
                print order
                if subbies:
                    for sub in subbies:
                        recip = sub.recipient
                        print recip
                        if recip is not None:
                            print "we got recip in a sub"
                            recip.user = user
                            recip.save()
                        else:
                            pass
                main_recipient = order.main_recipient
                if main_recipient is not None:
                    main_recipient.user = user
                    print main_recipient
                    main_recipient.save()
                else:
                    pass

                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    context = {
        "form": form,

    }

    template = "accounts/signup.html"
    return render(request, template, context)

class DashTemplateView(TemplateView):

    template_name = 'accounts/dashboard.html'

    # def get_context_data(self, **kwargs):
    #     context = super(DashTemplateView, self).get_context_data(**kwargs)
    #     context['client'] = Client.objects.get(user=self.request.user)
    #     return context
