# Generated by Django 2.1.4 on 2018-12-29 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_auto_20181229_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept', to='account.Department'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='account.Subject'),
        ),
    ]
