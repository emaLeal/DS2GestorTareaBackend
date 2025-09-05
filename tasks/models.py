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
    is_active = models.BooleanField(default=True)

    # --- AUDITORIA MINIMA---
    # Estos campos permiten rastrear *cuándo* y *por quién* se creó o actualizó la tarea.

    created_at = models.DateTimeField(auto_now_add=True) # fecha de creación
    # Guarda automáticamente la fecha y hora en que la tarea fue creada. 
    # Se llena solo una vez y NO vuelve a cambiar.


    updated_at = models.DateTimeField(auto_now=True) # fecha de última actualización
    # Se actualiza automáticamente cada vez que la tarea es modificada.
    # Django lo gestiona de forma interna, no requiere intervención manual.


    created_by = models.ForeignKey( User, on_delete=models.SET_NULL, null=True, related_name="tasks_created" )
    # Usuario que registró la tarea por primera vez.
    # Importante: este campo no lo llena el usuario en un formulario,
    # sino que en la vista se asigna automáticamente usando `request.user`.
    # Ejemplo en una vista:
    #   task.created_by = request.user


    updated_by = models.ForeignKey( User, on_delete=models.SET_NULL, null=True, related_name="tasks_updated" )
    # Último usuario que modificó la tarea.
    # Al igual que `created_by`, NO lo llena el usuario desde el frontend.
    # Se asigna en la vista cuando alguien edita una tarea:
    #   task.updated_by = request.user


    class Meta:
        db_table = "Task"  # Nombre de la tabla en la BD

    def __str__(self):
        return self.title
