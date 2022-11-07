from .models import Place
from users.models import write_cities_db, write_regions_db
from django.shortcuts import render


def place_category_selector(request):
    return render(request, 'where_to_go/category_selector.html')
