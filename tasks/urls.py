# from django.urls import path, include
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register('', views.TaskView)

# urlpatterns = [
#     path('', include(router.urls))
# ]

from django.urls import path
from tasks import views

urlpatterns = [
  path('hello-view/', views.HelloApiView.as_view()),
]