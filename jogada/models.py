from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import User 
from django.utils import timezone
from jogo.models import Jogo, Tabuleiro, Posicao 

class Jogada(models.Model):
	jogo = models.ForeignKey(Jogo, related_name="jogada_jogo")
	autor = models.ForeignKey(User, related_name="jogada_autor")
	adversario = models.ForeignKey(User, related_name='jogada_adversario')
	linha = models.CharField(max_length=2)
	coluna = models.CharField(max_length=2)	
	registro = models.DateTimeField(default=timezone.now)
	teste = models.CharField(max_length=2)
	acerto = models.BooleanField(default=False)

	def __str__(self):
		return "Jogada de " + self.autor.username + " contra " + self.adversario.username + " realizada no dia " + self.registro.strftime('%d %B %Y') + " : linha " + self.linha + ", coluna " + self.coluna