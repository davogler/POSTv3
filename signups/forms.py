from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm


class ConnectForm(forms.Form):
    
    email_signup = forms.EmailField(
      required = True,
      label = 'Sign Up. Stay Connected:',
      initial='Your Email',
      
    )
    
    def addError(self, message):
      self._errors[NON_FIELD_ERRORS] = self.error_class([message])
      
