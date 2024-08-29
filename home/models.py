from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Usuarios(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    usuario = models.CharField(max_length=50)
    semestre = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    
    class Meta:
        db_table="user"

class Archivos(models.Model):
    nombre_archivo = models.CharField(max_length=255)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "archivos"
        
class ActividadChatbot(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha_registro = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "actividad_chatbot"


class CalificacionRespuesta(models.Model):
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    fecha_calificacion = models.DateField(auto_now_add=True)  # Nuevo campo de fecha

    class Meta:
        db_table = "calificaciones_respuestas"