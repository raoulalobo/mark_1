# Generated by Django 3.1.2 on 2020-11-13 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_date_ajout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='date_ajout',
        ),
        migrations.AddField(
            model_name='client',
            name='dateheure',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
