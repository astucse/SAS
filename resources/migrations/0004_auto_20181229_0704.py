# Generated by Django 2.1.4 on 2018-12-29 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('resources', '0003_auto_20181228_1733'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Videos',
            new_name='Video',
        ),
    ]
