# Generated by Django 3.1.6 on 2021-02-21 14:07

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210221_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location),
        ),
    ]
