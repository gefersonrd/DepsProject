from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import request
from gerenciador_fornecedor.models import *
from gerenciador_fornecedor.forms import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

def index(request):
	#return HttpResponse("Projeto")
	lista_itens = Fornecedor.objects.all()
	lista_itens_endereco = Endereco.objects.all()
	return render_to_response("index.html", {'lista_itens': lista_itens, 'lista_itens_endereco': lista_itens_endereco})

def adiciona(request):
	if request.POST: #formulario enviado
		form = ContactForm(request.POST)
		if form.is_valid():

			#formulario valido
			dados = form.cleaned_data#armazena no dicionario
			item = Fornecedor(nome=dados['nome'], telefone=dados['telefone'], descricao=dados['descricao'], data=None, hora=None )
			item.save()#salva no banco de dados
			return HttpResponseRedirect('/')

			#return render_to_response("salvo.html",{})
	else: #pagina acessada via link metodo get
		#exibe o formulario em branco
		form = ContactForm()
	return render(request, 'adiciona.html', {'form': form})
	#render_to_response("adiciona.html", {'form':form}, context_instance=RequestContext(request))


def item(request, nr_item):
	#try:
		#item = Fornecedor.objects.get(pk= nr_item)
	item = get_object_or_404(Fornecedor, pk= nr_item)
	#except Fornecedor.DoesNotExist:
		#raise Http404()
	return render_to_response('item.html', {'item': item})
	#except:
		#pass