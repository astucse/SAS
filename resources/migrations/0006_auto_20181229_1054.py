# Generated by Django 2.1.4 on 2018-12-29 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20181229_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Department'),
        ),
        migrations.AlterField(
            model_name='video',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Subject'),
        ),
    ]
