# Generated by Django 3.1.2 on 2020-11-13 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0003_auto_20201103_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enquete',
            options={'ordering': ['voyage__dateheure']},
        ),
        migrations.AddField(
            model_name='enquete',
            name='dateheure',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 13, 11, 43, 2, 885407)),
        ),
    ]
