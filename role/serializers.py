from rest_framework import serializers
from role.models import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'description']
        extra_kwargs = {
            'id': {
                'required': False,  # Hacer el ID opcional
                'allow_null': True,  # Permitir valores null
                'read_only': False   # Permitir escribir el ID cuando se proporcione
            }
        }

