# Generated by Django 3.2.8 on 2021-10-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211025_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdb',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
