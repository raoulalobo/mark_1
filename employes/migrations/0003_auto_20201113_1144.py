# Generated by Django 3.1.2 on 2020-11-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employes', '0002_employe_date_ajout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='date_ajout',
        ),
        migrations.AddField(
            model_name='employe',
            name='dateheure',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
