from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register('v1/profile', views.UserProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('v1/profile/login/', views.UserLoginApiView.as_view()),
    path('v1/current_user/', get_current_user),
    path('v1/users/create', CreateUserView.as_view()),
    path('v1/login/', obtain_jwt_token)
]
