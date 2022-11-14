from django import forms
from users.models import Region, City
from .models import Place


class SearchCityForm(forms.Form):
    region = forms.ModelChoiceField(
        queryset=Region.objects.all())

    city = forms.CharField(max_length=100)

    def get_city_obj(self):
        cleaned_data = self.cleaned_data
        city = cleaned_data.get('city')
        region = cleaned_data.get('region')

        self.region = region
        self.city = city

        global city_obj
        city_obj = None
        print(cleaned_data)

        if (city and region) is not None:
            city_obj = City.objects.\
                filter(region=region).filter(name=city)

        else:
            self.add_error('city', 'Не указан нас. пункт или регион')

            return city_obj

    def valid_city(self) -> bool:
        try:
            self.get_city_obj()
            print('form is valid')
            return True

        except:
            return False


class PlaceForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    kitchen_type = forms.CharField(
        required=False, max_length=100)

    class Meta:
        model = Place
        fields = ('name', 'address',
                  'category', 'open_time', 'close_time')
