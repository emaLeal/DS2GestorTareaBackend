from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.get_roles),
    path('create/', views.create_role),
    path('update/<int:id>/', views.update_role),
    path('delete/<int:id>/', views.delete_role),
]