# Generated by Django 2.2.3 on 2019-08-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0004_auto_20190808_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetooneroom',
            name='limitation',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
