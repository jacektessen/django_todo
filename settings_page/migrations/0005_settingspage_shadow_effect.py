# Generated by Django 2.2.7 on 2019-12-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_page', '0004_auto_20191222_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingspage',
            name='shadow_effect',
            field=models.BooleanField(default=False),
        ),
    ]