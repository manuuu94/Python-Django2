# Generated by Django 4.1.4 on 2023-05-31 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gptApp', '0002_alter_randq_answer_alter_randq_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randq',
            name='answer',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='randq',
            name='question',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
