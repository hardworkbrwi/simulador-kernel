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
    
    # o metodo possui um erro. Pois ele está com dois processos iguais
    # no escalonamento.
    def escalonarProcessos( self, memoriaPrimaria ):
        ordemDosProcessos = [ [] for _ in range(4) ]
        item = 0

        while item < len( memoriaPrimaria.posicoesMemoria ):
            processo = memoriaPrimaria.posicoesMemoria[ item ]
            ordemDosProcessos[ processo.prioridade ].append( processo )
            item = item + processo.tamanhoProcesso - 1
        
        for processos in ordemDosProcessos:
            for processo in processos:
                processo.exibirInfoProcesso()
        pass

