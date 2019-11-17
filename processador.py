#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#processador.py

from processo import Processo

class Processador:
    __slots__ = [ "_tabelaDeExecucaoDeProcessos", "_nivelAtualDePrioridade" ]

    def __init__( self ):
        self._tabelaDeExecucaoDeProcessos = [ [] for _ in range(5) ]
        self._nivelAtualDePrioridade = 0

    def executar( self, processo ):
        tempoDeVidaInicial = processo.tempoVida
        processo.tempoVida = processo.tempoVida - 2

        print( "Está sendo executado o processo com id: " , processo.idProcesso )

        if processo.tempoVida <= 0:
            return -1
        elif tempoDeVidaInicial == processo.tempoVida:
            return 0 

        self.adicionarProcessoNaTabelaDeExecucaoDeProcessos( processo )
        
        return 1
    
    def montarTabelaDeExecucaoDeProcessos( self, memoriaPrimaria ):
        item = 0

        for processos in self._tabelaDeExecucaoDeProcessos:
            processos.clear()

        while item < len( memoriaPrimaria.posicoesMemoria ):
            processo = memoriaPrimaria.posicoesMemoria[ item ]
            self._tabelaDeExecucaoDeProcessos[ processo.prioridade ].append( processo )
            item = item + processo.tamanhoProcesso

    def adicionarProcessoNaTabelaDeExecucaoDeProcessos( self, processo ):
        self._tabelaDeExecucaoDeProcessos[ self._nivelAtualDePrioridade ].append( processo )

    def escalonadorDeProcesso( self ):
        procurarProcesso = True

        while procurarProcesso and self._nivelAtualDePrioridade <= 4:
            if self.nivelAtualEstaVazia():
                self._nivelAtualDePrioridade = self._nivelAtualDePrioridade + 1

            elif self.nivelAtualEstaVazia() and self._nivelAtualDePrioridade == 4:
                self._nivelAtualDePrioridade = self._nivelAtualDePrioridade + 1

            else:
                procurarProcesso = False
        
        if self._nivelAtualDePrioridade < 5:
            return self._tabelaDeExecucaoDeProcessos[ self._nivelAtualDePrioridade ].pop(0)
        else:
            return None
        
    def nivelAtualEstaVazia( self ):
        if len( self._tabelaDeExecucaoDeProcessos[ self._nivelAtualDePrioridade ] ) == 0:
            return True
        else: 
            return False
    
    def tabelaDeExecucaoDeProcessosEstaVazia( self ):
        estaVazia = True

        for processos in self._tabelaDeExecucaoDeProcessos:
            if len( processos ) > 0:
                estaVazia = False
                break
        
        return estaVazia

    def exibirTabelaDeExecucaoDeProcessos( self ):
        contadorDeNivel = 0

        for processos in self._tabelaDeExecucaoDeProcessos:
            print( "Processos com nivel de prioridade: ", contadorDeNivel )
            for processo in processos:
                processo.exibirInfoProcesso()
                print("\n")
            print("---------------------------------")
            contadorDeNivel = contadorDeNivel + 1
