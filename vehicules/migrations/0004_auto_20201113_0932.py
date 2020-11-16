# Generated by Django 3.1.2 on 2020-11-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicules', '0003_vehicule_type_de_voiture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicule',
            name='type_de_voiture',
            field=models.CharField(choices=[('B', 'Bus'), ('P', 'Personnel'), ('G', 'Groupe'), ('N', 'Navette')], default='B', max_length=1),
        ),
    ]
