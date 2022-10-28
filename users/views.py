from django.shortcuts import redirect, render
from users.models import User
from django.contrib.auth.hashers import check_password
from .forms import ChangedUserCreationForm, UserAppendingForm, LoginForm
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user

from datetime import date, datetime

from russian_regions_and_cities.cortage_generator import get_region_full_name


def register(request):
    if request.method == 'POST':
        form = ChangedUserCreationForm(request.POST)
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

        allow_politics_and_processing = cleaned_data.get(
            'allow_politics_and_processing')

        print(request.POST)

        birthdate = cleaned_data.get('birthdate')
        birthdate_strfed = cleaned_data.get('birthdate').strftime('%Y-%m-%d')

        print(liveplace)

        def valid_age(age: date) -> bool:
            today = datetime.now().date()
            days_of_life = (today-age).days

            if days_of_life > 0:
                return True
            else:
                return False

        if (allow_politics_and_processing == True) and (valid_age(birthdate)):
            created_user = User.objects.create_user(
                username=email, password=pw1, email=email, phonenum=phonenum, name=name, liveplace=liveplace, surname=surname, patronymic=patronymic, birthdate=birthdate_strfed, region=region, allow_politics_and_processing=allow_politics_and_processing)

            print(created_user)

            login_user(request, user=created_user)
            return redirect('/register2')

        else:
            return redirect('/register')

    return render(request, 'registration/register.html', {'form': ChangedUserCreationForm()})


def user_append(request):
    append_form = UserAppendingForm
    user = request.user

    if request.method == 'POST':
        form = UserAppendingForm(request.POST, request.FILES, instance=user)

        photo = request.FILES.get('photo')
        print(photo)

        form.save(commit=False)

        if form.is_valid():
            form.save()

            return redirect('/')
        else:
            print('form is invalid')

    return render(request, 'registration/append_user.html', {'form': append_form})


def login_select(request):
    return render(request, 'registration/login_select.html')


def login(request, login_method):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            email = cleaned_data.get('email')
            phonenum = request.POST.get('phonenum')
            password = cleaned_data.get('password')

            global founded_user
            founded_user = ''

            if email and login_method == 'email':
                try:
                    founded_user = User.objects.filter(email=email)[0]
                except:
                    return redirect(f'/login/{login_method}')

            elif phonenum and login_method == 'phonenum':
                try:
                    founded_user = User.objects.filter(phonenum=phonenum)[0]
                except:
                    return redirect(f'/login/{login_method}')

            if check_password(password, founded_user.password):
                login_user(request, user=founded_user)

                return redirect('/')
            else:
                return redirect(f'/login/{login_method}')

    return render(request, 'registration/login.html', {'form': LoginForm(), 'login_method': login_method})


def logout(request):
    logout_user(request)

    return redirect('/register')


def delete_user(request):
    user = request.user

    if request.method == 'POST':
        print(request.POST)
        logout_user(request)
        user.delete()

        return redirect('/register')

    return render(request, 'registration/delete_user.html')


def cabinet(request):
    return render(request, 'registration/cabinet.html')
