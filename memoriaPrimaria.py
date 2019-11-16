#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#memoriaPrimaria.py

class MemoriaPrimaria:
    '''
    Define um objeto abstraindo a memória primaria do computador
    '''

    __slots__ = [ "_posicoesMemoria", "_tamanhoMemoria" ]

    def __init__( self, tamanhoMemoria = 2048 ):
        # Tamanho da memória principal em kilobytes (KB)
        self._tamanhoMemoria = tamanhoMemoria
        self._posicoesMemoria = []
        

    def adicionarProcessoMemoria( self, processo, posicaoInicial, tamanhoPagina = None ):
        espacoUtilizadoMemoria = len( self._posicoesMemoria )
        
        if( tamanhoPagina == None ):
            tamanhoProcessoNovo = processo.tamanhoProcesso
        else:
            tamanhoProcessoNovo = tamanhoPagina

        if espacoUtilizadoMemoria + tamanhoProcessoNovo <= self._tamanhoMemoria:
            posicaoFinal = posicaoInicial + tamanhoProcessoNovo
            for i in range( posicaoInicial, posicaoFinal ):
                self._posicoesMemoria.insert( i, processo )

            return True
            
        else:
            return False

        

    def liberarMemoria( self, tamanhoPagina = None ):
        # ALTERAR PARA USAR MÉTODO DE SUBSTITUIÇÃO DE PÁGINA LRU
        processoASerRemovido = self._posicoesMemoria[0]

        if( tamanhoPagina == None ):
            tamanhoProcessoASerRemovido = processoASerRemovido.tamanhoProcesso

        else:
            tamanhoProcessoASerRemovido = tamanhoPagina
            
        for i in range( tamanhoProcessoASerRemovido - 1, -1, -1 ):
            del( self._posicoesMemoria[i] )
        
        #processoASerRemovido.tempoVida -= processoASerRemovido.tempoExecucao

        return processoASerRemovido

    def exibirMemoriaPrimariaTamanhoTotalProcesso( self ):
        """
		Exibe os processos inseridos na memória primária
		"""
        print( "-------- ALOCAÇÃO DA MEMÓRIA PRINCIPAL --------".center(52) )
        LINHA = "-"
        grade = 52 * LINHA
        print( "{}".format( grade ) )
        print( "{}|{}|{}".format( "INTERVALO DE POSIÇÕES".center(22),
                                  "ID PROCESSO".center(12),
                                  "TAMANHO PROCESSO".center(16) ) )
        print( grade )
        
        ultimoProcessoTemp = self._posicoesMemoria[-1]
        tamanhoProcessoTemp = ultimoProcessoTemp.tamanhoProcesso
        posicaoAtual = 0
        quantidadePosicoesOcupadas = len( self._posicoesMemoria )
        posicaoFinal = quantidadePosicoesOcupadas - tamanhoProcessoTemp
        
        while( posicaoAtual <= posicaoFinal ):
            processo = self._posicoesMemoria[ posicaoAtual ]
            print( "{}-{}|{}|{}".format( str( posicaoAtual ).ljust(10), str( posicaoAtual + processo.tamanhoProcesso - 1 ).rjust(11),
                                    str( processo.idProcesso ).ljust(12),
                                    str( processo.tamanhoProcesso).ljust(16) ) )
            
            posicaoAtual += processo.tamanhoProcesso

        print( grade )

    def exibirMemoriaPrimariaTamanhoPagina( self, tamanhoPagina ):
        """
		Exibe os processos inseridos na memória primária
		"""
        print( "-------- ALOCAÇÃO DA MEMÓRIA PRINCIPAL --------".center(52) )
        LINHA = "-"
        grade = 52 * LINHA
        print( "{}".format( grade ) )
        print( "{}|{}|{}".format( "INTERVALO DE POSIÇÕES".center(22),
                                  "ID PROCESSO".center(12),
                                  "TAMANHO PÁGINA".center(16) ) )
        print( grade )
        
        posicaoAtual = 0
        quantidadePosicoesOcupadas = len( self._posicoesMemoria )
        posicaoFinal = quantidadePosicoesOcupadas - tamanhoPagina
        
        while( posicaoAtual <= posicaoFinal ):
            processo = self._posicoesMemoria[ posicaoAtual ]
            print( "{}-{}|{}|{}".format( str( posicaoAtual ).ljust(10), str( posicaoAtual + tamanhoPagina - 1 ).rjust(11),
                                    str( processo.idProcesso ).ljust(12),
                                    str( tamanhoPagina).ljust(16) ) )
            
            posicaoAtual += tamanhoPagina

        print( grade )
    
    @property
    def posicoesMemoria( self ):
        return self._posicoesMemoria

    @property
    def tamanhoMemoria( self ):
        return self._tamanhoMemoria


    