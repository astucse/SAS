# Generated by Django 2.1.4 on 2018-12-30 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20181230_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.OneToOneField(default=True, max_length=50, on_delete=django.db.models.deletion.CASCADE, to='account.Department'),
        ),
    ]
