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
@permission_classes([IsAuthenticated])
def get_tasks(request):
    queryset = Task.objects.filter(is_active=True)

    # Filtros por query params
    user_id = request.query_params.get('user_id')
    status_value = request.query_params.get('status')
    priority_value = request.query_params.get('priority')
    created_by_id = request.query_params.get('created_by_id')
    tag = request.query_params.get('tag')

    if user_id:
        queryset = queryset.filter(user_id=user_id)
    if status_value:
        queryset = queryset.filter(status=status_value)
    if priority_value:
        queryset = queryset.filter(priority=priority_value)
    if created_by_id:
        queryset = queryset.filter(created_by_id=created_by_id)
    if tag:
        queryset = queryset.filter(tags__contains=[tag])

    # Paginacin
    from rest_framework.pagination import PageNumberPagination
    paginator = PageNumberPagination()
    page = paginator.paginate_queryset(queryset.order_by('-created_at'), request)
    serializer = TaskSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)

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
    user = request.user  # Usuario autenticado
    data = request.data.copy()

    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save(created_by=user, updated_by=user)  # 🔹 Se asignan aquí
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
        serializer.save(updated_by=request.user)  # 🔹 Actualiza solo el campo updated_by
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
