# Generated by Django 2.2.7 on 2019-12-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20191130_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='order_no',
            field=models.IntegerField(default=-1),
        ),
    ]
