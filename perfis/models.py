from django.db import models

class Perfil(object):
    def __init__(self,nome='',email='',senha='',senhaRepete=''):
        self.nome=nome
        self.email=email
        self.senha=senha
        self.senhaRete=senhaRepete
# Create your models here.
