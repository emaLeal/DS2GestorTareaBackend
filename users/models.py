from django.db import models
from django.contrib.auth.models import AbstractUser
from department.models import Department
from role.models import Role

# Create your models here.
class User(AbstractUser):

    # username = None
    first_name = models.CharField(max_length=130, default="")
    last_name = models.CharField(max_length=130, default="")
    document_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='users')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')

    # Eliminamos campos redundantes, AbstractUser ya tiene username, password, email
    # Puedes añadir más si lo necesitas: phone, address, etc.

    class Meta:
        db_table = "User"

    def __str__(self):
        return f"{self.username} "