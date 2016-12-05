from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from jogo.models import Jogo, Tabuleiro, Posicao

class BatalhaNaval(object):
    def __init__(self):
        self.tabuleiro = {}

    def tabuleiroGerar(self, jogo):
        tab = Tabuleiro(jogo=jogo, tamanho=5)
        tab.save()

        barco = False

        for posI in range(tab.tamanho):
            for posJ in range(tab.tamanho):
                if (posI == 1 and posJ == 1) or (posI == 2 and posJ == 2) or (posI == 3 and posJ == 3):
                    barco = True
                else:
                    barco = False

                Posicao(linha=posI, coluna=posJ, barco=barco, tabuleiro=tab).save()

        return tab

    def tabuleiroAtualizar(self, jogada):
        tabuleiro = Tabuleiro.objects.get(jogo=jogada.jogo)

        # define posição como verificada e se é um acerto
        posicao = get_object_or_404(Posicao, tabuleiro=tabuleiro, linha=jogada.linha, coluna=jogada.coluna)
        posicao.verificado = True
        if posicao.barco == True:
            posicao.acerto = True
        else:
            posicao.acerto = False

        jogada.acerto = posicao.acerto
        posicao.save()
        jogada.save()

    def permiteJogada(self, jogada):
        autor = jogada.autor      
        
        if jogada.jogo.jogadasJogador1 < jogada.jogo.jogadasMaxima:
            return  True
        else:
            return False

    def jogoAtualizar(self, jogada):
        jogador = jogada.autor
        jogo = jogada.jogo        

        if jogo.jogador1 == jogador:
            jogo.jogadasJogador1 += 1
        else:
            jogo.jogadasJogador2 += 1
                
        jogo.save()

    def atualizar(self, jogada):

        if self.permiteJogada(jogada):
            self.tabuleiroAtualizar(jogada)
            self.jogoAtualizar(jogada)

    def getMatriz(self, jogo):
        tabuleiro = get_object_or_404(Tabuleiro, jogo=jogo)
        posicoes = Posicao.objects.filter(tabuleiro=tabuleiro)
    	
        matriz = [[Posicao() for i in range(5)] for j in range(5)]

        for pos in posicoes:
            matriz[pos.linha][pos.coluna].barco = True

        return matriz