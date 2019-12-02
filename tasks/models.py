from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib import admin


class Tasks(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255, default="")
    column = models.CharField(max_length=255, default="column2")
    order_no = models.IntegerField(default=99)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

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


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email
