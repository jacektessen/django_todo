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
                "panel_1": settings.panel_1,
                "panel_2": settings.panel_2,
                "panel_3": settings.panel_3,
                "panel_4": settings.panel_4,
                "language": settings.language,
                "user": settings.user.id
            }
        }
        return Response(response)
