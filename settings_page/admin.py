from django.contrib import admin

from settings_page import models


class SettingsPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'panel_1_color', 'panel_2_color', 'panel_3_color',
                    'panel_4_color', 'language', 'user', 'user_id')
    list_display_links = ('id', 'user', 'user_id')
    list_filter = ("id", "user", "user_id")
    list_per_page = 50


admin.site.register(models.SettingsPage, SettingsPageAdmin)
