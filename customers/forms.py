from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML, Button
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

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

    def __init__(self, *args, **kwargs):
        super(RecipientAddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.add_input(Submit("submit", "Add this Recipient"))
        #self.helper.add_input(HTML('<a class="btn btn-warning" href={% url "checkout" %}>Cancel</a>'))
        self.helper.layout = Layout(
            Fieldset(
                '{{form_title}}',
                "first_name",
                  "last_name",
                  "org",
                  "address_line1",
                  "address_line2",
                  "city",
                  "state_province",
                  "country",
                  "postal_code"
            ),
            FormActions(
              Submit('save_changes', '{{submit_btn}}', css_class="btn-primary pcta"),
              Button('cancel', 'Cancel', css_class="btn-default pcta", onclick="window.history.back()"),
              
        ),
            
            
        )
        


