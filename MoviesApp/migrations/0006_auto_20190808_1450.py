# Generated by Django 2.2.3 on 2019-08-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesApp', '0005_auto_20190808_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='igdb_id',
            field=models.CharField(max_length=8),
        ),
    ]
