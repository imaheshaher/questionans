# Generated by Django 3.0 on 2019-12-19 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20191219_1804'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
    ]