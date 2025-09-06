from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.get_departments),
    path('create/', views.create_department),
    path('update/<int:id>/', views.update_department),
    path('delete/<int:id>/', views.delete_department),
]