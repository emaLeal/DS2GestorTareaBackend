from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    

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
            'user'  ,
            'is_active',
            # 'created_by',   # <-- AGREGADO
            # 'updated_by'    # <-- AGREGADO
        ]