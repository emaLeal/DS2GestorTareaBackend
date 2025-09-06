from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'priority',
            'start_date',
            'due_date',
            'user'  ,
            'is_active'
                  ]