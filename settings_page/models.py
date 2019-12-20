from django.db import models
from user.models import UserProfile

LANGUAGES = (
    ("EN", "english"),
    ("PL", "polish"),
    ("NO", "norwegian")
)


class SettingsPage(models.Model):
    panel_1 = models.CharField(max_length=255, default="#ffcc80")
    panel_2 = models.CharField(max_length=255, default="#fff176")
    panel_3 = models.CharField(max_length=255, default="#ffeef2")
    panel_4 = models.CharField(max_length=255, default="lightGreen")
    language = models.CharField(
        max_length=255, choices=LANGUAGES, default="EN")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
