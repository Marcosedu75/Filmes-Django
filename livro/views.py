from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm # Precisaremos criar este arquivo e formulário

def home(request):
    return render(request, 'home.html')

# Create your views here.
def listar_livros(request):
    """Busca todos os livros no banco de dados e os exibe em uma página."""
    livros = Livro.objects.all()
    context = {'livros': livros}
    return render(request, 'listar_livro.html', context)

def cadastrar_livro(request):
    """Permite cadastrar um novo livro."""
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list') # Redireciona para a lista após o cadastro
    else:
        form = LivroForm() # Cria um formulário vazio para exibição

    context = {'form': form}
    return render(request, 'cadastrar_livro.html', context)
