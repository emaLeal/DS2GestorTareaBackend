from django.db import models

class Role(models.Model):
    '''Model for the role the user will be assigned with'''
    # El ID se genera automáticamente por Django (AutoField es el default para pk)
    description = models.CharField(max_length=20, default="Postulant")

    class Meta:
        db_table = "Role"
    
    def __str__(self):
        return self.description