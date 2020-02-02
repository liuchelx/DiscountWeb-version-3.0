# Generated by Django 3.0.2 on 2020-01-24 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=200)),
                ('PubTime', models.DateTimeField()),
                ('EndTime', models.DateTimeField()),
                ('OriPrice', models.FloatField(default=0)),
                ('DisPrice', models.FloatField(default=0)),
                ('Shoplink', models.URLField(max_length=500)),
                ('imglink', models.URLField(max_length=500)),
                ('Tag', models.CharField(max_length=200)),
                ('click', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default_pic.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
