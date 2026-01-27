from django.db import models

# Create your models here.

class Funcionario(models.Model):
    funcionario_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    idade = models.IntegerField
    cpf = models.CharField(max_length=11, unique=True)
    funcao = models.CharField(max_length=100)
    admin = models.BooleanField()
    def __str__(self):
        return self.nome