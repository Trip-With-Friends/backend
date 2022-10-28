import os
from datetime import datetime
from uuid import uuid4
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver

from russian_regions_and_cities.cortage_generator import *


class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True)
    surname = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=50, default='')
    patronymic = models.CharField(
        max_length=50, blank=True, null=True, default='')
    birthdate = models.DateField(
        editable=True, null=False, default='2000-01-01')
    photo = models.ImageField(null=True, upload_to='users_thumbnails')

    email = models.EmailField(unique=True)
    phonenum = PhoneNumberField(region=None, unique=True)
    region = models.CharField(
        max_length=5,
        choices=gen_regions_list(),
        blank=False,
        null=False,
        default=''
    )

    liveplace = models.CharField(max_length=50, blank=False, default='')
    description = models.TextField(blank=True, max_length=1000)
    not_twf_exp = models.TextField(blank=True, max_length=1000)
    allow_politics_and_processing = models.BooleanField(default=False)

    def get_age(self) -> int:
        today = datetime.now().date()
        days_of_life = (today-self.birthdate).days

        return days_of_life//365

    def get_region_full_name(self) -> str:
        short_name = self.region
        full_name = get_region_full_name(short_name)

        return full_name

    def get_photo_path(self) -> str:
        photo = self.photo
        photo_basename = os.path.basename(photo.name)
        path = f'/media/users_thumbnails/{photo_basename}'

        return path


@receiver(models.signals.pre_delete, sender=User)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.photo:
        instance.photo.delete(False)
