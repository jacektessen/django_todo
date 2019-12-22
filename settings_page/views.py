from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SettingsPageSerializer
from .models import SettingsPage


class SettingsPageView(viewsets.ModelViewSet):
    queryset = SettingsPage.objects.all()
    serializer_class = SettingsPageSerializer


class UsersSettings(APIView):
    def get(self, request, format=None):
        settings = SettingsPage.objects.get(user=request.user.id)

        response = {
            "model": "SettingsPage",
            "settings": {
                "panel_1_color": settings.panel_1_color,
                "panel_2_color": settings.panel_2_color,
                "panel_3_color": settings.panel_3_color,
                "panel_4_color": settings.panel_4_color,
                "panel_1_name": settings.panel_1_name,
                "panel_2_name": settings.panel_2_name,
                "panel_3_name": settings.panel_3_name,
                "panel_4_name": settings.panel_4_name,
                "shadow_effect": settings.shadow_effect,
                "language": settings.language,
                "user": settings.user.id,
                "id": settings.id
            }
        }
        return Response(response)
