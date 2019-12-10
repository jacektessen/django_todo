from django.contrib import admin

from tasks import models


admin.site.register(models.Tasks)
admin.site.register(models.Columns, models.columnsAdmin)
