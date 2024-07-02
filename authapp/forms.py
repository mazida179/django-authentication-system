from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_changed


class RegisterUser(UserCreationForm):
    first_name = forms.CharField()
    error_css_class = "error"
    required_css_class = "required"



    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_active', 'is_staff']
    
class MyForm(forms.Form):
    birth_years = ['2010', '2011', '2012']
    # birth_day = forms.DateField(widget=forms.SelectDateWidget(years=birth_years) )

    birth_day = forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
)




    