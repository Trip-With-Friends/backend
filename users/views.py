from datetime import date, datetime

from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user

from .forms import ChangedUserCreationForm,\
    UserAppendingForm, LoginForm
from users.models import User

from errors_utils.errors_processing import gen_errors_list


def register(request):
    '''
    Страница регистрации
    '''
    errors_list = []

    if request.method == 'POST':
        form = ChangedUserCreationForm(request.POST)

        form_is_valid = form.is_valid()
        no_form_custom_errors = form.custom_errors_catching(request)

        print(form_is_valid)
        print(no_form_custom_errors)

        if form.is_valid() and form.custom_errors_catching(request):
            print('form is valid')
            form.save(commit=False)

            cleaned_data = form.cleaned_data
            print(f'{cleaned_data}')

            pw1 = cleaned_data.get('password1')

            email = cleaned_data.get('email')
            phonenum = request.POST.get('phonenum')

            name = cleaned_data.get('name')
            surname = cleaned_data.get('surname')
            patronymic = cleaned_data.get('patronymic')

            region = cleaned_data.get('region')
            liveplace = request.POST.get('liveplace')

            birthdate_strfed = cleaned_data.get('birthdate')\
                .strftime('%Y-%m-%d')

            created_user = User.objects.create_user(
                username=email, password=pw1, email=email,
                phonenum=phonenum, name=name,
                liveplace=liveplace,
                surname=surname, patronymic=patronymic,
                birthdate=birthdate_strfed,
                region=region,
                allow_politics_and_processing=True)

            print(created_user)

            login_user(request, user=created_user)

            return redirect('/register2')

        else:
            print('not valid')
            errors_as_data = form.errors.as_data()
            errors_list = gen_errors_list(errors_as_data)

    else:
        form = ChangedUserCreationForm()

    return render(request, 'registration/register.html',
                  {'form': form, 'errors_list': errors_list})


def user_append(request):
    '''
    Дополнение пользователя описанием и фотографией
    '''
    user = request.user

    if request.method == 'POST':
        form = UserAppendingForm(
            request.POST, request.FILES, instance=user)

        photo = request.FILES.get('photo')
        print(photo)

        form.save(commit=False)

        if form.is_valid():
            form.save()

            return redirect('/')
        else:
            return redirect('/register2')

    return render(request, 'registration/append_user.html',
                  {'form': UserAppendingForm()})


def login_select(request):
    '''
    Выбор метода входа в аккаунт (по номеру телефона или email)
    '''
    return render(request, 'registration/login_select.html')


def login(request, login_method):
    '''
    Вход в аккаунт выбранным методом (см. login_select)
    '''
    errors_list = []

    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())

        if form.is_valid() and form.get_user(login_method):
            founded_user = form.get_user(login_method)
            print(type(founded_user))

            login_user(request, founded_user)
            return redirect('/')

        else:
            errors_as_data = form.errors.as_data()
            print(errors_as_data)
            errors_list = gen_errors_list(errors_as_data)
            print(f'errors_list is {errors_list}')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html',
                  {'form': form,
                   'login_method': login_method,
                   'errors_list': errors_list})


def logout(request):
    '''
    Выход и аккаунта
    '''
    logout_user(request)

    return redirect('/register')


def delete_user(request):
    '''
    Удаление аккаунта
    '''
    user = request.user

    if request.method == 'POST':
        print(request.POST)
        logout_user(request)
        user.delete()

        return redirect('/register')

    return render(request, 'registration/delete_user.html')


def cabinet(request):
    '''
    Личный кабинет
    '''
    return render(request, 'registration/cabinet.html')
