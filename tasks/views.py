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
    return Response(serializer.data, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task_user(request):
    user = request.user
    tasks = Task.objects.filter(user=user, is_active=True)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    user = request.user
    data = request.data.copy()
    data['user'] = user.id
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def patch_task(request, document_id):
    try:
        task = get_object_or_404(Task, pk=document_id)
    except task.DoesNotExist:
        return Response({"error": "No encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    data = data.request.copy()
    serializer = TaskSerializer(instance=task, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, document_id):
    try:
        task = get_object_or_404(Task, pk=document_id)
    except task.DoesNotExist:
        return Response({"error": "No encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    data = {
        "is_active": False 
    }
    serializer = TaskSerializer(instance=task, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"La tarea fue eliminada exitosamente"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
