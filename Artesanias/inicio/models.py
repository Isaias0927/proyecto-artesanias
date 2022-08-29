from django.db import models

# Create your models here.
class Artesanias(models.Model): #Define la estructura de nuestra tabla
    nombre = models.TextField(max_length=20,verbose_name="Nombre Artesania") #Texto corto
    descripcion = models.TextField(max_length=500,verbose_name="Descripción general") #Texto largo
    foto = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    municipio = models.TextField(max_length=50,verbose_name="Municipio de origen")
    costo = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Artesania"
        verbose_name_plural = "Artesanias"
        ordering = ["-created"] 
    def __str__(self):
        return self.nombre

class OpinionArtesania(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    artesania = models.CharField(max_length=100, verbose_name="Nom Artesania")
    opinion = models.TextField(verbose_name="Opinión")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Opinion de Artesania"
        verbose_name_plural = "Opiniones de Artesanias"
        ordering = ["-created"]
        
        def __str__(self):
            return self.artesania