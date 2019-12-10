from rest_framework import serializers
from tasks import models


class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tasks
        fields = '__all__'


class ColumnsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Columns
        fields = '__all__'
