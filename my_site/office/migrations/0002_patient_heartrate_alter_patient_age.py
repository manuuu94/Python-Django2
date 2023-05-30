# Generated by Django 4.1.4 on 2023-05-23 21:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='heartrate',
            field=models.IntegerField(default=60, validators=[django.core.validators.MinLengthValidator(20), django.core.validators.MaxLengthValidator(300)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(20), django.core.validators.MaxLengthValidator(300)]),
        ),
    ]
