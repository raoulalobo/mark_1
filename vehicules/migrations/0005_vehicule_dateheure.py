# Generated by Django 3.1.2 on 2020-11-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicules', '0004_auto_20201113_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='dateheure',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
