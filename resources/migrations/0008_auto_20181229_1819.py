# Generated by Django 2.1.4 on 2018-12-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_handout_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handout',
            name='file',
            field=models.FileField(upload_to='Handouts/'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='file',
            field=models.FileField(upload_to='Slides/'),
        ),
    ]