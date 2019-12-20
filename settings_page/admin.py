from django.contrib import admin

from settings_page import models


class SettingsPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'panel_1', 'panel_2', 'panel_3',
                    'panel_4', 'language', 'user', 'user_id')
    list_display_links = ('id', 'user', 'user_id')
    list_filter = ("id", "user", "user_id")
    list_per_page = 50


admin.site.register(models.SettingsPage, SettingsPageAdmin)
