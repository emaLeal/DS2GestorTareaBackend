from django.db import models
from django.contrib.auth.models import AbstractUser
from department.models import Department
from role.models import Role
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):

    username = None
    first_name = models.CharField(max_length=130, default="")
    last_name = models.CharField(max_length=130, default="")
    document_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='users', default=1)
    identification_type = models.CharField(max_length=2, default="")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)


    # Eliminamos campos redundantes, AbstractUser ya     tiene username, password, email
    # Puedes añadir más si lo necesitas: phone, address, etc.
    USERNAME_FIELD = 'document_id'

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'email',
        'role',
        'department',
        'identification_type'
        ]
    objects = CustomUserManager()

    class Meta:
        db_table = "User"

    def __str__(self):
        return f"{self.document_id} "