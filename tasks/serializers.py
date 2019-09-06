from rest_framework import serializers
from .models import Task

# class TaskSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Task
#     fields = '__all__'


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


