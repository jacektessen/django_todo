from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks import views

router = DefaultRouter()
router.register('v1/tasks', views.TasksView)
router.register('v1/columns', views.ColumnsView)


urlpatterns = [
    path('v2/tasks/', views.ListTasks.as_view()),
    path('v2/tasks/<int:task_id>', views.TaskById.as_view()),
    path('', include(router.urls))
]
