from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.shortcuts import get_object_or_404
from .models import Task
from rest_framework import status
from .serializers import TaskSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_tasks(request):
    tasks = Task.objects.filter(is_active=True)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task_user(request):
    user = request.user
    tasks = Task.objects.filter(user=user, is_active=True)
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_task(request):
    # user = request.user
    print(request.data)
    data = request.data.copy()
    # data['user'] = user.id
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def patch_task(request, id):
    # Buscar la tarea por su ID
    task = get_object_or_404(Task, pk=id)
    # Copiar los datos del request
    data = request.data.copy()
    # Serializar y actualizar parcialmente
    serializer = TaskSerializer(instance=task, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    
    # Eliminación lógica (marcar como inactiva)
    task.is_active = False
    task.save(update_fields=['is_active'])

    return Response(
        {"message": "La tarea fue eliminada exitosamente"},
        status=status.HTTP_200_OK
    )
