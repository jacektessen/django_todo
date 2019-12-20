# Generated by Django 2.2.7 on 2019-12-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingspage',
            name='language',
            field=models.CharField(choices=[('EN', 'english'), ('PL', 'polish'), ('NO', 'norwegian')], default='EN', max_length=255),
        ),
    ]
