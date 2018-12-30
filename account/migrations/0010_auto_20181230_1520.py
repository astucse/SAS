# Generated by Django 2.1.4 on 2018-12-30 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20181230_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.ForeignKey(default=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.School'),
        ),
    ]
