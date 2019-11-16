#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#segmento.py

from statusSegmento import StatusSegmento

class Segmento:
    '''
    Posicao da lista do mapa de bits
    '''

    __slots__ = [ "_processo", "_posicaoInicial", "_quantidadePosicoes", "_classeSubstituicaoPagina" ]

    def __init__( self ):
        self._quantidadePosicoes = 0
        self._classeSubstituicaoPagina = -1

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
        return self._classeSubstituicaoPagina

    def definirClasseSubstituicaoPagina( self ):
        if( self._processo.bitR == 0 and self._processo.bitM == 0 ):
            self._classeSubstituicaoPagina = 0
        
        elif( self._processo.bitR == 0 and self._processo.bitM == 1 ):
            self._classeSubstituicaoPagina = 1
        
        elif( self._processo.bitR == 1 and self._processo.bitM == 0 ):
            self._classeSubstituicaoPagina = 2

        elif( self._processo.bitR == 1 and self._processo.bitM == 1 ):
            self._classeSubstituicaoPagina = 3

        else:
            self._classeSubstituicaoPagina = -1
    