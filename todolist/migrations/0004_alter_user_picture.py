# Generated by Django 5.0.1 on 2024-02-15 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Picture',
            field=models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg'])]),
        ),
    ]
