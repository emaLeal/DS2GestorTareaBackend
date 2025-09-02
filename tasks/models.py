from django.db import models
from users.models import User  # Asumiendo que tienes un modelo de usuario en users.models

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('completed', 'Completada'),
    ]

    PRIORITY_CHOICES = [
        ('high', 'Alta'),
        ('medium', 'Media'),
        ('low', 'Baja'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    start_date = models.DateField()
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="id")  # Usuario que crea la tarea

    class Meta:
        db_table = "Task"  # Nombre de la tabla en la BD

    def __str__(self):
        return self.title
