# Generated by Django 4.1.9 on 2023-06-30 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_cv', '0014_alter_skills_yearspractice'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='progress',
            field=models.IntegerField(default=50, max_length=3),
            preserve_default=False,
        ),
    ]