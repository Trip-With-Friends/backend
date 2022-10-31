from datetime import datetime, date
from tkinter import font

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password

from .models import User
from phonenumber_field.formfields import PhoneNumberField
from russian_regions_and_cities.regions_utils import valid_liveplace, get_region_full_name


class ChangedUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['surname', 'name', 'patronymic',
                  'birthdate', 'email', 'phonenum',
                  'region', 'liveplace',
                  'allow_politics_and_processing']

    def custom_errors_catching(self, request):
        cleaned_data = self.cleaned_data

        allow_politics = request.POST.get(
            'allow_politics_and_processing')
        birthdate = cleaned_data.get('birthdate')
        region = cleaned_data.get('region')
        liveplace = cleaned_data.get('liveplace')

        print(cleaned_data)

        if not allow_politics:
            self.add_error(
                "allow_politics_and_processing",
                "Вы не принимаете политику конфиденциальности и обработку данных"
            )

        # Проверка корректности возраста
        def valid_age(age: date) -> bool:
            today = datetime.now().date()
            days_of_life = (today-age).days

            if days_of_life > 0:
                return True
            else:
                return False

        if not valid_age(birthdate):
            self.add_error(
                "birthdate",
                "Дата рождения введена неверно"
            )

        region_full_name = get_region_full_name(region)

        # Проверка корректности места жительства
        if not valid_liveplace(
                region_full_name, liveplace):
            self.add_error(
                "liveplace",
                "Такого города/села/деревни нет в базе данных"
            )

        if not self.errors:
            return True
        else:
            return False


class UserAppendingForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['photo', 'description', 'not_twf_exp']


class LoginForm(forms.Form):
    email = forms.EmailField(required=False)
    phonenum = PhoneNumberField(required=False)
    password = forms.CharField(
        max_length=50, widget=forms.PasswordInput)

    def get_user(self, login_method: str) -> User or None:
        cleaned_data = self.cleaned_data

        email = cleaned_data.get('email')
        phonenum = cleaned_data.get('phonenumdfas')
        password = cleaned_data.get('password')

        founded_user = None

        # Поиск пользователя
        if email and login_method == 'email':
            try:
                founded_user = User.objects\
                    .filter(email=email)[0]

            except:
                self.add_error(
                    'email', 'Пользователь с таким email не зарегистрирован')
                return None

        elif phonenum and login_method == 'phonenum':
            try:
                founded_user = User.objects\
                    .filter(phonenum=phonenum)[0]

            except:
                self.add_error(
                    'phonenum', 'Пользователь с таким номером телефона не зарегистрирован')
                return None

        # Проверка корректности пароля
        if founded_user:
            if check_password(password, founded_user.password):
                return founded_user
            else:
                self.add_error('password', 'Неверный пароль')
                return None
