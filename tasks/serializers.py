from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.first_name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.first_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.first_name', read_only=True)

    findAt = serializers.DateField(source='start_date', input_formats=['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S.%fZ'])
    closedAt = serializers.DateField(source='due_date', input_formats=['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S.%fZ'])

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'priority',
            'findAt',
            'closedAt',
            'user',
            'user_name',
            'created_by_name',
            'updated_by_name',
            'created_at',
            'updated_at',
            'is_active',
            'tags'
        ]