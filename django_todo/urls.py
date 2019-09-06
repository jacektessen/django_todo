from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('api/v1/tasks/', include('tasks.urls')),
# ]

urlpatterns = [
    path('api/', include('tasks.urls'),)
]