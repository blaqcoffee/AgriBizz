# Generated by Django 3.1.6 on 2021-03-21 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_practiceintro_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practiceintro',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/blog/'),
        ),
    ]