from django.shortcuts import render

# Create your views here.
def tela_cadastro_de_clientes(request):
    return render(request, 'tela_cadastro_de_clientes.html', {})