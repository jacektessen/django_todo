from django.contrib import admin

from user import models


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'is_active')
    list_display_links = ('id', 'email', "name")
    list_filter = ('email', "name")
    list_editable = ('is_active',)
    search_fields = ('email', 'name')
    list_per_page = 50


admin.site.register(models.UserProfile, UsersAdmin)
