# Generated by Django 2.1.4 on 2019-01-14 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_no',
            field=models.CharField(default='aur', max_length=40),
        ),
    ]
