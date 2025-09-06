from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register),
    path('get_profile/', views.get_profile),
    path('users/getall/', views.get_users),
    path('update/<str:document_id>/', views.update_user),  
    path('delete/<str:document_id>/', views.delete_user),  
    path('change_password/', views.change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls'), name='password_reset')
]