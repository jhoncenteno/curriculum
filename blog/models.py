from django.db import models

# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()                  
    fecha = models.DateTimeField(blank=True)        

    created = models.DateTimeField(auto_now_add=True)   
    updated = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.titulo