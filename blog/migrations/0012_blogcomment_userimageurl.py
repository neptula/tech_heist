# Generated by Django 3.2.8 on 2021-11-15 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20211110_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='userImageUrl',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
