# Generated by Django 3.1.6 on 2021-03-07 13:51

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_author_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='body',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=tinymce.models.HTMLField(default=True),
            preserve_default=False,
        ),
    ]