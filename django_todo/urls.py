from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('api/v1/tasks/', include('tasks.urls')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls'),)
]