from django.db import models
from django.contrib.auth.models import User
from blog.models import Employee

# Create your models here.

class TipoCita(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nombre")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now = True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Tipo de cita"
        verbose_name_plural = "Tipos de citas"

    def __str__(self):
        return self.name
    

class Cita(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, verbose_name="Empleado", on_delete=models.CASCADE, default="" )
    typeof = models.ForeignKey(TipoCita, verbose_name="Tipo de cita", on_delete=models.CASCADE, default="")
    date = models.DateTimeField(verbose_name="Para el")
    status = models.SmallIntegerField(verbose_name="Estado de la cita", default=2)
    comments = models.TextField(verbose_name="Comentario", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now = True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"

