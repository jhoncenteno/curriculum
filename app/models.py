from django.db import models

class Proyectos(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='proyectos')
    url = models.URLField(blank=True)                   
    created = models.DateTimeField(auto_now_add=True)   
    updated = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return self.titulo

