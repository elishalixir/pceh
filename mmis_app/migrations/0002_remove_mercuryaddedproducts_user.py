# Generated by Django 4.1.2 on 2022-10-22 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmis_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mercuryaddedproducts',
            name='user',
        ),
    ]
