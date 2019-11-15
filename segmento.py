#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#segmento.py

from statusSegmento import StatusSegmento

class Segmento:
    '''
    Posicao da lista do mapa de bits
    '''

    __slots__ = [ "_processo", "_posicaoInicial", "_quantidadePosicoes", "_classeSubstituicao" ]

    def __init__( self ):
        self._quantidadePosicoes = 0
        self._classeSubstituicao = -1

    @property
    def processo( self ):
        return self._processo
    
    @processo.setter
    def processo( self, processo ):
        self._processo = processo

    @property
    def posicaoInicial( self ):
        return self._posicaoInicial
    
    @posicaoInicial.setter
    def posicaoInicial( self, posicaoInicial ):
        self._posicaoInicial = posicaoInicial

    @property
    def quantidadePosicoes( self ):
        return self._quantidadePosicoes
    
    @quantidadePosicoes.setter
    def quantidadePosicoes( self, quantidadePosicoes ):
        self._quantidadePosicoes = quantidadePosicoes

    @property
    def classeSubstituicao( self ):
        return self._classeSubstituicao

    def definirClasseSubstituicao( self, processoBitR, processoBitM ):
        if( processoBitR == 0 and processoBitM == 0 ):
            self._classeSubstituicao = 0
        
        elif( processoBitR == 0 and processoBitM == 1 ):
            self._classeSubstituicao = 1
        
        elif( processoBitR == 1 and processoBitM == 0 ):
            self._classeSubstituicao = 2

        elif( processoBitR == 1 and processoBitM == 1 ):
            self._classeSubstituicao == 3

        else:
            self._classeSubstituicao = -1
    