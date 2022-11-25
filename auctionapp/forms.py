from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Layout, Submit
from crispy_forms.bootstrap import FormActions

class Login(forms.Form):

    email = forms.EmailField(
        label = 'Email',
        max_length= 250,
        widget=forms.TextInput(attrs={'autocomplete': 'Email'})
    )

    password = forms.CharField(
        label='Password',
        max_length=250,
        widget=forms.PasswordInput(attrs={'autocomplete': 'password'})
    )

    helper = FormHelper()
    helper.form_id = 'login-form'
    helper.layout = Layout(
        Row('email', css_class="mb-2"),
        Row('password', css_class="mb-2"),
        FormActions(
            Submit('login', 'Log in', css_class="mt-2"),
        )
    )



