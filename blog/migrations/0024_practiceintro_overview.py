# Generated by Django 3.1.6 on 2021-03-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20210322_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='practiceintro',
            name='overview',
            field=models.CharField(default='', max_length=45),
        ),
    ]
