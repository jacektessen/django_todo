from rest_framework import serializers
from settings_page import models


class SettingsPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SettingsPage
        fields = '__all__'
