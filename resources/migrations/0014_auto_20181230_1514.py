# Generated by Django 2.1.4 on 2018-12-30 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0013_merge_20181230_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='answer_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='resources.Question'),
        ),
    ]
