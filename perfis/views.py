from django.shortcuts import render
from perfis.models import Perfil



def index(request):
    return render(request,'index.html')

def exibir(request):
    perfil = Perfil()
    perfil = Perfil("Peba",'peba@peba.com.br','123','123')

    return render(request,'perfil.html',{"perfil":perfil})

# Create your views here.
