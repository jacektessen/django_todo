from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication
from tasks import permissions
from rest_framework import filters

from .models import Tasks, Columns
from .serializers import TasksSerializer, ColumnsSerializer


class TasksView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.AccessToOwnTasks,)
    # permission_classes = (IsAuthenticated,)

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('id', 'user_id',)


class ColumnsView(viewsets.ModelViewSet):
    queryset = Columns.objects.all()
    serializer_class = ColumnsSerializer


class ListTasks(APIView):

    def get(self, request, format=None):
        count = Tasks.objects.filter(user=request.user.id).count()
        print("request user", request.user.id)
        print("count", count)
        tasks = []
        for value in Tasks.objects.filter(user=request.user.id):
            print("value", value.user.id)
            data_value = {
                "id": value.id,
                "name": value.name,
                "content": value.content,
                "column": value.column,
                "order_no": value.order_no,
                "created at": value.created_at,
                "completed": value.completed,
                "user_id": value.user.id
            }

            tasks.append(data_value)

        an_apiview = {
            "ok": True,
            "data": {
                "tasks":
                tasks,
                "users": []
            },
            "total_count_tasks": count
        }

        return Response(an_apiview)


class TaskById(APIView):

    def get(self, request, task_id, format=None):
        value = Tasks.objects.get(id=task_id)
        if request.user.id != value.user.id:
            return Response("No Permission")

        task = {
            "model": "Task",
            "task": {
                "id": value.id,
                "name": value.name,
                "content": value.content,
                "column": value.column,
                "created at": value.created_at,
                "completed": value.completed,
                "user": value.user.id
            }
        }

        return Response(task)
