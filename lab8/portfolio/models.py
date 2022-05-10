from django.db import models

# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]