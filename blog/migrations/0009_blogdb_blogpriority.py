# Generated by Django 3.2.8 on 2021-11-05 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogdb_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdb',
            name='blogpriority',
            field=models.IntegerField(default=0),
        ),
    ]
