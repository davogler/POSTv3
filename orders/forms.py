from django import forms

from django.contrib.auth import get_user_model


User = get_user_model()

from orders.models import Order

class PayForm(forms.Form):
    last_4_digits = forms.CharField(
        required=False,
        min_length=4,
        max_length=4,
        widget=forms.HiddenInput()
    )

    stripe_token = forms.CharField(
        required=False,
        widget=forms.HiddenInput()
    )

    #name = forms.CharField()

    #password = forms.CharField(
    #        required = False,
    #        widget = forms.PasswordInput()
    #    )

