from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Nombre")
    description = models.CharField(max_length=250,verbose_name="Descripcion")
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now = True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100,verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default="null",verbose_name="Imagen",upload_to="articles")
    public = models.BooleanField(verbose_name="¿Publicado?")
    #on_delete CASCADE significa que se va a borrar todo en cascada si borras el usuario, se borrara el articulo etc
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE, editable=False)
    categories = models.ManyToManyField(Category,verbose_name="Categorias", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now = True, verbose_name="Actualizado el")  

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-created_at']

    def __str__(self):
        return self.title  

class Employee(models.Model):
    first_name = models.CharField(max_length=50,verbose_name="Nombre")
    last_name = models.CharField(max_length=50,verbose_name="Apellido")
    user = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE, editable=False)
    profession = models.CharField(max_length=50,verbose_name="Profesion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now = True, verbose_name="Actualizado el")  

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name 

"""class Notification(models.Model):
    status = models.BooleanField
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now = True, verbose_name="Actualizado el") """

