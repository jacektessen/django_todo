# Generated by Django 2.2.7 on 2019-12-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20191217_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='content',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
