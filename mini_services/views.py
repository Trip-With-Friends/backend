from django.shortcuts import render
from .forms import CalculatorForm


def menu(request):
    return render(request, 'menu.html')


def calculator(request):
    global calculated
    calculated = None

    if request.method == 'POST':
        form = CalculatorForm(request.POST)

        if form.is_valid():
            calculated = form.calculate()

    elif request.method == 'GET':
        form = CalculatorForm()

    return render(request, 'calculator.html',
                  {'form': form,
                   'calculated': calculated})
