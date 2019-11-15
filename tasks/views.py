from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .models import Task
from tasks import serializers
from .serializers import TaskSerializer
from tasks import models
from tasks import permissions


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class ListTasks(APIView):
  
  def get(self, request, format=None):
    count = Task.objects.all().count()
    tasks = []
    for value in Task.objects.all():

      data_value = {
          "id": value.id,
          "name": value.name,
          "content": value.content,
          "column": value.column,
          "created at": value.created_at,
          "completed": value.completed,
          "user_id": "user.id"
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
    tasks = {}
    value = Task.objects.get(id=task_id)
    count = Task.objects.all().count()

    tasks[value.id] = {
      "model": "Task",
      "length": count,
      "tasks": {
        "id": value.id,
        "name": value.name,
        "content": value.content,
        "column": value.column,
        "created at": value.created_at,
        "completed": value.completed,
      }
    }

    return Response(tasks)




class HelloApiView(APIView):
  """Test API View"""
  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """Returns a list of APIView features"""

    an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your logic',
        'Is mapped manually to URLs',
    ]

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})

  def post(self, request):
    """Create a hello message with our name"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'
      return Response({'message': message})
    else:
      return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
        )

  def put(self, request, pk=None):
      """Handle updating an object"""

      return Response({'method': 'PUT'})

  def patch(self, request, pk=None):
      """Handle partial update of object"""

      return Response({'method': 'PATCH'})

  def delete(self, request, pk=None):
      """Delete an object"""

      return Response({'method': 'DELETE'})    



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)



class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

