# Generated by Django 2.2.7 on 2019-12-20 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_1', models.CharField(default='#ffcc80', max_length=255)),
                ('panel_2', models.CharField(default='#fff176', max_length=255)),
                ('panel_3', models.CharField(default='#ffeef2', max_length=255)),
                ('panel_4', models.CharField(default='lightGreen', max_length=255)),
                ('language', models.IntegerField(choices=[(1, 'EN'), (2, 'PL'), (3, 'NO')], default=1)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
