# Generated by Django 3.1.2 on 2020-11-13 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voyages', '0004_auto_20201113_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voyage',
            options={'ordering': ['dateheure']},
        ),
        migrations.RenameField(
            model_name='voyage',
            old_name='date_voyage',
            new_name='dateheure',
        ),
    ]
