# Generated by Django 3.2.8 on 2021-10-22 14:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
