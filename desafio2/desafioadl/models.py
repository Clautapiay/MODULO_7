from django.db import models

# Create your models here.

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.descripcion
    
class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    tarea_id = models.ForeignKey('Tarea', on_delete=models.CASCADE)

    def __str__(self):
        return 'Tarea: ' + self.tarea_id.descripcion + ' - SubTarea: ' + self.descripcion
