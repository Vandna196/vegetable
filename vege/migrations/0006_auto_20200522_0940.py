# Generated by Django 3.0.3 on 2020-05-22 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_auto_20200521_1043'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bill',
        ),
        migrations.DeleteModel(
            name='Cartotal',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
