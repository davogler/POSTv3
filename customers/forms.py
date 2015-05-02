from django import forms

from django.contrib.auth import get_user_model


User = get_user_model()

from customers.models import Recipient


class RecipientAddressForm(forms.ModelForm):
    #default = forms.BooleanField(label='Make Default')

    class Meta:
        model = Recipient
        fields = ["first_name",
                  "last_name",
                  "org",
                  "address_line1",
                  "address_line2",
                  "city",
                  "state_province",
                  "country",
                  "postal_code"]
