# Generated by Django 3.2.7 on 2021-09-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
