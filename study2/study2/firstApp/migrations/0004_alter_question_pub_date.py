# Generated by Django 5.0.6 on 2024-05-17 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 17, 14, 42, 5, 155269), verbose_name='date published'),
        ),
    ]