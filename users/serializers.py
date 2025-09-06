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
            'email',
            'role_id',
            'identification_type',
            'role_description'
                  ]
        extra_kwargs = {
            "password": {"write_only": True}  # para no devolverla en la respuesta
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data, password=password)
        return user

class ChangePasswordSerializer(serializers.Serializer):
    document_id = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)