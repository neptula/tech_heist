# Generated by Django 3.2.8 on 2021-11-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogdb_blogpriority'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdb',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='static/images/%y'),
            preserve_default=False,
        ),
    ]
