# Generated by Django 5.0.1 on 2024-02-15 10:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Phone',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]