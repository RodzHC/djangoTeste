from django.db import models

# python manage.py makemigrations
# ->Comando para criar o arquivo de banco de dados basiado no schema
# python manage.py migration
# ->comando para implementar as migracoes que foram criadas com o makemigration

class Perfil(models.Model):
        nome = models.CharField(max_length=255, null=255)
        email = models.CharField(max_length=255, null=255)
        telefone = models.CharField(max_length=255, null=255)
        nome = models.CharField(max_length=255, null=255)

# Create your models here.
