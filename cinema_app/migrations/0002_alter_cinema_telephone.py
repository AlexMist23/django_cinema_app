# Generated by Django 4.1.3 on 2022-12-05 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='telephone',
            field=models.IntegerField(),
        ),
    ]
