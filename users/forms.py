from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput
from .models import User
from phonenumber_field.formfields import PhoneNumberField


class ChangedUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['surname', 'name', 'patronymic',
                  'birthdate', 'email', 'phonenum', 'region', 'liveplace', 'allow_politics_and_processing']


class UserAppendingForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['photo', 'description', 'not_twf_exp']


class LoginForm(forms.Form):
    email = forms.EmailField(required=False)
    phonenum = PhoneNumberField(required=False)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
