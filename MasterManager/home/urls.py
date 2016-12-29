from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'', views.home_page),
    url(r'^CadastroDeClientes/', views.tela_cadastro_de_clientes),
]