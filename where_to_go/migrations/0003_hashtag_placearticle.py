# Generated by Django 4.0.3 on 2022-11-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_go', '0002_alter_place_kitchen_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150)),
                ('text', models.TextField(max_length=10000)),
                ('hashtags', models.ManyToManyField(to='where_to_go.hashtag')),
            ],
        ),
    ]
