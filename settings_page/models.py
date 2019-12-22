from django.db import models
from user.models import UserProfile

LANGUAGES = (
    ("EN", "english"),
    ("PL", "polish"),
    ("NO", "norwegian")
)


class SettingsPage(models.Model):
    panel_1_color = models.CharField(max_length=255, default="#ffcc80")
    panel_2_color = models.CharField(max_length=255, default="#fff176")
    panel_3_color = models.CharField(max_length=255, default="#ffeef2")
    panel_4_color = models.CharField(max_length=255, default="#90ee90")
    panel_1_name = models.CharField(max_length=255, default="Important")
    panel_2_name = models.CharField(max_length=255, default="Normal")
    panel_3_name = models.CharField(max_length=255, default="Later")
    panel_4_name = models.CharField(max_length=255, default="Done")
    language = models.CharField(
        max_length=255, choices=LANGUAGES, default="EN")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
