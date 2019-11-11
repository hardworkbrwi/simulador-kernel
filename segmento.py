#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#segmento.py

from statusSegmento import StatusSegmento

class Segmento:
    '''
    Posicao da lista do mapa de bits
    '''

    __slots__ = [ "_processo", "_posicaoInicial", "_quantidadePosicoes" ]

    def __init__( self ):
        self._quantidadePosicoes = 0

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
    