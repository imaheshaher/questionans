# Generated by Django 3.0 on 2019-12-19 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20191219_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
    ]
