from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.get_tasks),
    path('get-task-user/', views.get_task_user),
    path('create/', views.create_task),
    path('patch/<str:document_id>/', views.patch_task),
    path('delete/<str:document_id>/', views.delete_task)
]