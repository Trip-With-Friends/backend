import os
from django.db import models
from django.dispatch import receiver


class PlaceCategory(models.Model):
    name = models.CharField(max_length=100, blank=False)
    code_name = models.CharField(max_length=100, blank=False, default='')

    def __str__(self):
        return self.name

    def get_text_name(self) -> str:
        return self.name.lower()


class Place(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=200, blank=False)
    open_time = models.CharField(max_length=20, blank=True)
    close_time = models.CharField(max_length=20, blank=True)

    # kitchen type only in cafe or restaurant!
    kitchen_type = models.CharField(
        max_length=100, blank=True, null=True)

    city = models.ForeignKey(
        'users.City', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(
        'PlaceCategory', on_delete=models.SET_NULL, null=True)


class PlaceImage(models.Model):
    place = models.ForeignKey(
        'Place', on_delete=models.CASCADE, blank=False)
    image = models.ImageField(
        blank=False, upload_to='places_images')

    def get_path(self):
        photo_basename = os.path.basename(self.image.name)

        return f'media/places_images/{photo_basename}'


class SocialThumbnail(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(
        blank=False, upload_to='socials_thumnails')

    def __str__(self):
        return self.name


class PlaceLink(models.Model):
    link = models.URLField(max_length=200)
    social_image = models.ForeignKey(
        'SocialThumbnail', on_delete=models.SET_NULL,
        null=True, blank=True)
    social = models.CharField(max_length=20, blank=True)

    place = models.ForeignKey(
        'Place', on_delete=models.CASCADE,
        null=False, blank=False, default=None)

    def __str__(self):
        return self.link


class Hashtag(models.Model):
    hashtag = models.CharField(
        max_length=50, blank=False, null=False)

    def __str__(self):
        return f'#{self.hashtag}'

    def is_valid(self) -> bool:
        exception_symbols = ['~', ':', "'", '+', '[', '\\',
                             '@', '^', '{', '%', '(', '-', '"', '*', '|', ',',
                             '&', '<', '`', '}', '.', '=', ']', '!', '>',
                             ';', '?', '#', '$', ')', '/']

        for symbol in self.hashtag:
            if symbol in exception_symbols:
                return False

        return True


class PlaceArticle(models.Model):
    header = models.CharField(
        max_length=150, blank=False, null=False)
    text = models.TextField(
        max_length=10000, blank=False, null=False)

    hashtags = models.ManyToManyField('Hashtag')
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, default=None)
    city = models.ForeignKey(
        'users.City', on_delete=models.CASCADE, default=None)

    def get_hashtags_list(self) -> list:
        return [hashtag for hashtag in self.hashtags.values('hashtag').all()]


@receiver(models.signals.post_delete, sender=PlaceImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)


@receiver(models.signals.post_save, sender=PlaceLink)
def set_social_thumbnail_and_field(sender, instance, **kwargs):
    link = instance.link
    social_name = link.split('https://')[1].split('.')[0]

    print(instance.social)

    instance.social = social_name

    try:
        thumbnail = SocialThumbnail.objects.filter(
            name=social_name)[0]
        instance.social_image = thumbnail
        instance.save()

    except:
        return None


@receiver(models.signals.post_save, sender=Place)
def set_kitchen_type(sender, instance, **kwargs):
    if instance.category.code_name != 'cafe':
        instance.kitchen_type = None

        print('kitchen is none')
