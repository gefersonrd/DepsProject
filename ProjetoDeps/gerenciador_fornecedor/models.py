from django.db import models

# Create your models here.

class Fornecedor(models.Model):
	nome = models.CharField(max_length=31)
	telefone = models.CharField(max_length=15)
	descricao = models.TextField()
	data = models.DateField()
	hora = models.TimeField()

	def __str__(self):
		return self.nome


class Endereco(models.Model):
	fornecedor = models.ForeignKey(Fornecedor)
	rua = models.CharField(max_length=21)
	pais = models.CharField(max_length=21)
	cidade = models.CharField(max_length=21)
	estado = models.CharField(max_length=21)

	def __str__(self):
		return self.rua
