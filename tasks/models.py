from django.db import models
from users.models import User  # Asumiendo que tienes un modelo de usuario en users.models
from django.contrib.postgres.fields import ArrayField

class Task(models.Model):
    STATUS_CHOICES = [
        ('To do', 'To do'),
        ('in-progress', 'En Progreso'),
        ('completed', 'Completada'),
    ]

    PRIORITY_CHOICES = [
        ('high', 'Alta'),
        ('medium', 'Media'),
        ('low', 'Baja'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To do')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    start_date = models.DateField()
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="id")  # Usuario que crea la tarea
    is_active = models.BooleanField(default=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True, default=list)

    # --- AUDITORIA MINIMA---
    # Estos campos permiten rastrear *cuándo* y *por quién* se creó o actualizó la tarea.

    created_at = models.DateTimeField(auto_now_add=True) # fecha de creación


    updated_at = models.DateTimeField(auto_now=True) # fecha de última actualización


    created_by = models.ForeignKey( User, on_delete=models.SET_NULL, null=True, related_name="tasks_created" )
    # Usuario que registró la tarea por primera vez.

    updated_by = models.ForeignKey( User, on_delete=models.SET_NULL, null=True, related_name="tasks_updated" )
    # Último usuario que modificó la tarea.


    class Meta:
        db_table = "Task"  # Nombre de la tabla en la BD

    def __str__(self):
        return self.title
