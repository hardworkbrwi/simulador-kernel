#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#processador.py

from processo import Processo

class Processador:

    def executar( self, processo ):
        tempoDeVidaInicial = processo.tempoVida
        processo.tempoVida = processo.tempoVida - 2

        print( "Está sendo executado o processo com id: " , processo.idProcesso )
        
        if processo.tempoVida <= 0:
            return -1
        elif tempoDeVidaInicial == processo.tempoVida:
            return 0 

        return 1

    def escalonarProcessos( self, memoria):
        pass

