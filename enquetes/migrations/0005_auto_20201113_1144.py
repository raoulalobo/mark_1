# Generated by Django 3.1.2 on 2020-11-13 11:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0004_auto_20201113_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquete',
            name='dateheure',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
