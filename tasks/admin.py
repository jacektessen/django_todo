from django.contrib import admin

from tasks import models


admin.site.register(models.UserProfile)
admin.site.register(models.Task)