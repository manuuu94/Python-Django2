# Generated by Django 4.1.9 on 2023-07-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gptApp', '0016_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
