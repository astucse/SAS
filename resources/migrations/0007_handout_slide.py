# Generated by Django 2.1.4 on 2018-12-29 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('resources', '0006_auto_20181229_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Handout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=55)),
                ('file', models.FileField(upload_to='Uploads/Handouts/')),
                ('section', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Department')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='Uploads/Slides/')),
                ('name', models.CharField(max_length=55)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Department')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Subject')),
            ],
        ),
    ]