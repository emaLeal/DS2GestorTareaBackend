from rest_framework import serializers
from .models import User
from department.models import Department
from role.models import Role

class UserSerializer(serializers.ModelSerializer):
    '''User Serializer to return json'''
    department_id = serializers.PrimaryKeyRelatedField(
        source='department', queryset=Department.objects.all()
    )
    role_id = serializers.PrimaryKeyRelatedField(
        source='role', queryset=Role.objects.all()
    )    
    role_description = serializers.CharField(source='role.description', read_only=True)
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'document_id',
            'department_id',
            'role_id',
            'role_description',
            'email',
                  ]

class ChangePasswordSerializer(serializers.Serializer):
    document_id = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)