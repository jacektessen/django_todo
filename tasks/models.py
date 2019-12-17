from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import BaseUserManager
from django.contrib import admin
from user.models import UserProfile


class Tasks(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255, default="")
    column = models.CharField(max_length=255, default="column2")
    order_no = models.IntegerField(default=-1)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name


class Columns(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    tasks_IDs = models.ManyToManyField(Tasks, through="Tasks_IDs_column")

    class Meta:
        verbose_name_plural = "Columns"

    def __str__(self):
        return self.name


class Tasks_IDs_column(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    column = models.ForeignKey(Columns, on_delete=models.CASCADE)


class tasks_IDs_column_inline(admin.TabularInline):
    model = Tasks_IDs_column
    extra = 1


class tasksAdmin(admin.ModelAdmin):
    inlines = (tasks_IDs_column_inline)


class columnsAdmin(admin.ModelAdmin):
    inlines = (tasks_IDs_column_inline,)
    list_display = ('id', 'name', 'title')
    list_display_links = ('id', 'title')
