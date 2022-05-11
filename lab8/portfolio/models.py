from django.db import models

# Create your models here.

class Post(models.Model):
  autor = models.CharField(max_length=100)
  titulo = models.CharField(max_length=200)
  descricao = models.CharField(max_length=500)
  link = models.CharField(max_length=200)
  imagem = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
  criado = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titulo[:50]

class PontuacaoQuizz(models.Model):
  nome = models.CharField(max_length=100)
  pontuacao = models.IntegerField(min_value=2, **options)
  criado = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.nome[:50]