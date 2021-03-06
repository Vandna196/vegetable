# Generated by Django 3.0.3 on 2020-05-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='First',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('register', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('isactive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('isactive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password1', models.CharField(max_length=255)),
                ('password2', models.CharField(max_length=255)),
                ('isactive', models.BooleanField()),
            ],
        ),
    ]
