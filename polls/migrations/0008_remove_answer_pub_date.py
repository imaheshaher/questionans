# Generated by Django 3.0 on 2019-12-19 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20191219_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='pub_date',
        ),
    ]
