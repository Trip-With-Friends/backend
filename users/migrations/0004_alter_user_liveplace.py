# Generated by Django 4.0.3 on 2022-11-06 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_city_region_delete_cities_city_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='liveplace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.city'),
        ),
    ]