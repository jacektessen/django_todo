from django.contrib import admin

from tasks import models


class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content', 'column', 'order_no',
                    'created_at', 'completed', 'user', 'user_id')
    list_display_links = ('id', 'name', "user", "user_id")
    list_filter = ('name', 'name', "created_at", "user", "user_id")
    list_editable = ('completed',)
    search_fields = ('name', 'user', 'user.id')
    list_per_page = 50


admin.site.register(models.Tasks, TasksAdmin)
admin.site.register(models.Columns, models.columnsAdmin)
