from django.shortcuts import redirect, render

from users.models import City, Region

from .forms import PlaceForm, SearchCityForm
from .models import PlaceArticle, PlaceCategory, PlaceImage


def city_selector(request, region_short_name, city_name):
    region_obj = None
    city_obj = None

    if request.method == 'POST':
        form = SearchCityForm(request.POST)

        if form.is_valid() and form.valid_city():
            print(f'bound is {form.is_bound}')

            city = form.city
            region = form.region

            return redirect('city_selector',
                            region_short_name=region.short_name.lower(),
                            city_name=city.lower())

        else:
            print(f'bound is {form.is_bound}')

    elif request.method == 'GET':
        form = SearchCityForm()

        if city_name and region_short_name is not None:
            city_is_selected = True

            region_obj = Region.objects.\
                only('short_name', 'id').\
                filter(short_name=region_short_name.upper())[0]

            city_obj = City.objects.\
                filter(region=region_obj).\
                select_related('region').\
                get(name=city_name.title())

        else:
            city_is_selected = False

    def get_last_article():
        if not city_is_selected:
            try:
                last_article = PlaceArticle.objects\
                    .only('header', 'id').last()

                print(last_article)

                return last_article

            except:
                return None

    def get_all_places():
        try:
            return city_obj.get_all_places_dict()

        except:
            print('city is none')

    return render(request, 'where_to_go/city_selector.html',
                  {'form': form,
                   'city_is_selected': city_is_selected,
                   'categories': PlaceCategory.objects.all().values('name', 'code_name'),
                   'first_article': get_last_article(),
                   'category_places_list': get_all_places(),
                   'city_name': city_name,
                   'region_name': region_short_name, })


def category_viewer(request, region_short_name, city_name, category):

    region_obj = Region.objects.\
        only('short_name', 'id').\
        filter(short_name=region_short_name.upper())[0]

    city_obj = City.objects.\
        filter(region=region_obj).\
        select_related('region').\
        get(name=city_name.title())

    places = city_obj.get_city_places(category)

    return render(request, 'where_to_go/category_viewer.html',
                  {'places': places,
                   'city_name': city_name,
                   'region_name': region_short_name, })


def create_place(request, region_short_name, city_name):
    region = Region.objects.filter(
        short_name=region_short_name.upper())[0]
    city = City.objects.filter(region=region)\
        .filter(name=city_name.title())[0]

    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)

        new_place = form.save(commit=False)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(cleaned_data)

            new_place.city = city
            new_place.save()

            if cleaned_data.get('image') is not None:
                print('image is not none')

                PlaceImage.objects.create(
                    place=new_place,
                    image=form.cleaned_data.get('image'))

            return redirect('cat_viewer',
                            region_short_name=region_short_name.upper(),
                            city_name=city_name.title(),
                            category=cleaned_data.get('category').code_name)

        else:
            print('form is invalid')

    else:
        form = PlaceForm()

    return render(request, 'where_to_go/create_place.html',
                  {'form': form,
                   'region': region_short_name,
                   'city': city_name})
