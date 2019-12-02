# from django.urls import path, include
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register('', views.TaskView)

# urlpatterns = [
#     path('', include(router.urls))
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('v1/tasks', views.TasksView)
router.register('v1/columns', views.ColumnsView)
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('v2/tasks/', views.ListTasks.as_view()),
    path('v2/tasks/<int:task_id>', views.TaskById.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
