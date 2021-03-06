# Generated by Django 2.1.4 on 2019-01-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20190114_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='section',
            field=models.PositiveIntegerField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(default=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.PositiveIntegerField(default=True, null=True),
        ),
    ]
