from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Role
from .serializers import RoleSerializer

@api_view(['GET'])
def get_roles(request):
    roles = Role.objects.all()
    serializer = RoleSerializer(roles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_role(request):
    data = request.data.copy()
    
    # Si no se proporciona ID, encontrar el primer ID disponible
    if 'id' not in data or data['id'] is None or data['id'] == '':
        # Encontrar el primer ID disponible (reutilizar IDs eliminados)
        next_id = find_next_available_id()
        data['id'] = next_id
    else:
        # Si se proporciona ID, verificar que no exista
        provided_id = data['id']
        if Role.objects.filter(id=provided_id).exists():
            return Response(
                {'id': ['Ya existe un rol con este ID.']}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    serializer = RoleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def find_next_available_id():
    """
    Encuentra el primer ID disponible, empezando desde 1.
    Reutiliza IDs de registros eliminados.
    """
    existing_ids = set(Role.objects.values_list('id', flat=True))
    
    # Empezar desde 1 y encontrar el primer número que no esté en uso
    next_id = 1
    while next_id in existing_ids:
        next_id += 1
    
    return next_id

@api_view(['PUT'])
def update_role(request, id):
    try:
        # Obtener el rol actual
        current_role = get_object_or_404(Role, pk=id)
        
        # Obtener los datos del request
        new_id = request.data.get('id')
        description = request.data.get('description')
        
        if new_id and int(new_id) != id:
            # Si el ID cambió, crear nuevo y eliminar el anterior
            # Verificar que el nuevo ID no exista
            if Role.objects.filter(id=new_id).exists():
                return Response(
                    {'error': 'Ya existe un rol con ese ID'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Crear el nuevo rol
            new_role = Role.objects.create(id=new_id, description=description)
            
            # Eliminar el rol anterior
            current_role.delete()
            
            # Serializar y retornar el nuevo rol
            serializer = RoleSerializer(new_role)
            return Response(serializer.data)
        else:
            # Si el ID no cambió, actualizar normalmente
            serializer = RoleSerializer(current_role, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['DELETE'])
def delete_role(request, id):
    try:
        role = Role.objects.get(id=id)
    except Role.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    role.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
