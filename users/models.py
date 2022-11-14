import os
from datetime import datetime
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver

from phonenumber_field.modelfields import PhoneNumberField
from russian_regions_and_cities.regions_utils import *
from russian_regions_and_cities.sources.russia_cities_dict import russia_cities_dict

from where_to_go.models import Place, PlaceCategory


class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True)
    surname = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=50, default='')
    patronymic = models.CharField(
        max_length=50, blank=True, null=True, default='')
    birthdate = models.DateField(
        editable=True, null=False, default='2000-01-01')
    photo = models.ImageField(null=True,
                              upload_to='users_thumbnails')

    email = models.EmailField(unique=True)
    phonenum = PhoneNumberField(region=None, unique=True)

    region = models.ForeignKey(
        'Region', on_delete=models.SET_NULL, null=True)
    liveplace = models.ForeignKey(
        'City', on_delete=models.SET_NULL, null=True)
    description = models.TextField(
        blank=True, max_length=1000)
    not_twf_exp = models.TextField(
        blank=True, max_length=1000)
    allow_politics_and_processing = models.BooleanField(
        default=False)

    def get_age(self) -> int:
        today = datetime.now().date()
        days_of_life = (today - self.birthdate).days

        return days_of_life // 365

    def get_photo_path(self) -> str:
        photo = self.photo
        photo_basename = os.path.basename(photo.name)
        path = f'/media/users_thumbnails/{photo_basename}'

        return path


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_city_places(self, category_code_name: str):
        try:
            cities_places = Place.objects.\
                filter(city=self).only('name', 'id')

            category = PlaceCategory.objects.filter(
                code_name=category_code_name).only('id')[0]

            return cities_places.filter(
                category=category)

        except:
            return None

    def get_all_places_dict(self) -> dict:
        try:
            cities_places = Place.objects.\
                filter(city=self).\
                select_related('name').\
                values('name')

            categories = PlaceCategory.objects.all()

            final_list = []

            for category in categories.iterator():
                cities_category_list = cities_places.\
                    filter(category=category)[:3]

                final_list.append({category: cities_category_list})

            return final_list

        except:
            return None


class Region(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


def write_regions_db(
        regions_list: list = russia_reg_dict):
    for region_dict in regions_list:
        for name, short_name in region_dict.items():
            Region.objects.create(
                name=name, short_name=short_name)

    print('regions written!')


def write_cities_db(
        cities_with_regions: list = russia_cities_dict):

    for region_cities_list in cities_with_regions:
        for region_name, cities_list in region_cities_list.items():
            region = Region.objects.filter(name=region_name)[0]

            for city in cities_list:
                City.objects.create(name=city, region=region)

    print('cities writen!')


@receiver(models.signals.pre_delete, sender=User)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.photo:
        instance.photo.delete(False)
