# Generated by Django 3.0 on 2019-12-15 09:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]