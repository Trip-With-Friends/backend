from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=200, blank=False)
    open_time = models.CharField(max_length=20, blank=True)
    close_time = models.CharField(max_length=20, blank=True)


class Restaurant(Place):
    kitchen_type = models.CharField(max_length=100, blank=False)


class Image(models.Model):
    name = models.CharField(max_length=100, blank=True)
    place = models.ForeignKey(
        'Place', on_delete=models.CASCADE, blank=False)
    image = models.ImageField(blank=False)
