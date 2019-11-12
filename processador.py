#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#processador.py

from processo import Processo

class Processador:
    __slots__ = [ "_tabelaDeExecucaoDeProcessos"]

    def __init__( self ):
        self._tabelaDeExecucaoDeProcessos = [ [] for _ in range(5) ]

    def executar( self, processo ):
        tempoDeVidaInicial = processo.tempoVida
        processo.tempoVida = processo.tempoVida - 2

        print( "Está sendo executado o processo com id: " , processo.idProcesso )

        if processo.tempoVida <= 0:
            return -1
        elif tempoDeVidaInicial == processo.tempoVida:
            return 0 

        return 1
    
    def montarTabelaDeExecucaoDeProcessos( self, memoriaPrimaria ):
        item = 0

        while item < len( memoriaPrimaria.posicoesMemoria ):
            processo = memoriaPrimaria.posicoesMemoria[ item ]
            self._tabelaDeExecucaoDeProcessos[ processo.prioridade ].append( processo )
            item = item + processo.tamanhoProcesso
    

    def atualizarTabelaDeExecucaoDeProcessos( self ):
        
        pass