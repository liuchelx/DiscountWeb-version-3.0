# Generated by Django 3.0.2 on 2020-01-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='wishlisted_products',
            field=models.ManyToManyField(to='discountsApp.Product'),
        ),
    ]
