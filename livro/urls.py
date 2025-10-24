from django.urls import path
from . import views

urlpatterns = [
    path('listar_livro/', views.listar_livros, name='livro_list'),
    path('cadastrar_livro/', views.cadastrar_livro, name='livro_cadastrar'),
]
