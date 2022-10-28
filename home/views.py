from django.shortcuts import redirect, render


def home(request):
    if request.user.id == None:
        return redirect('register')

    return render(request, 'home/home.html')
