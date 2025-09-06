from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']
        extra_kwargs = {
            'id': {
                'required': False,  # Hacer el ID opcional
                'allow_null': True,  # Permitir valores null
                'read_only': False   # Permitir escribir el ID cuando se proporcione
            }
        }

