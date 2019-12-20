from django.urls import path, include
from rest_framework.routers import DefaultRouter
from settings_page import views

router = DefaultRouter()
router.register('v1/settings', views.SettingsPageView)


urlpatterns = [
    path('', include(router.urls)),
    path('v2/settings/', views.UsersSettings.as_view())
]
