# Generated by Django 2.0.dev20170604010711 on 2017-09-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demandware', '0021_auto_20170920_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='language',
            field=models.CharField(default='', max_length=100),
        ),
    ]
