from django.db import models

# Create your models here.

class Fornecedor(models.Model):
	#cpf = models.CharField(max_length=31, primary_key=true)
	nome = models.CharField(max_length=31)
	telefone = models.CharField(max_length=15)
	descricao = models.TextField()
	data = models.DateField(null=True)
	hora = models.TimeField(null=True)
	#endereco = models.ForeignKey(Endereco)
	def __str__(self):
		return self.nome
	#class Meta:
		#db_table = "Fornecedor"

class Endereco(models.Model):
	fornecedor = models.ForeignKey(Fornecedor)
	rua = models.CharField(max_length=21)
	pais = models.CharField(max_length=21)
	cidade = models.CharField(max_length=21)
	estado = models.CharField(max_length=21)

	def __str__(self):
		return self.rua

	#class Meta:
		#db_table = "Endereco"


"""
{% for org in organisation %}
   <option value="{{org.id}}"
       {% if org == current_org %}selected="selected"{% endif %}>
       {{org.name|capfirst}}
   </option>
{% endfor %}
"""


