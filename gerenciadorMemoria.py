#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#gerenciadorMemoria.py

from mapeamentoEncadeadoBits import MapeamentoEncadeadoBits
from segmento import Segmento
from memoriaSecundaria import MemoriaSecundaria

class GerenciadorMemoria:

    """ Description	"""
    
    __slots__ = [ "_mapaBits", "_tamanhoPagina" ]

    def __init__( self, tamanhoPagina = None ):
        self._mapaBits = MapeamentoEncadeadoBits()
        self._tamanhoPagina = tamanhoPagina
    '''
    def adicionarProcessoMemoriaPrimaria( self, memoriaPrimaria, processo = None ):        

        if( processo == None ):
            self._removerProcessoMemoriaPrimaria( memoriaPrimaria, processo )

        else:        
            quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )
            tamanhoProcesso = processo.tamanhoProcesso
            tamanhoMaxMemoria = memoriaPrimaria.tamanhoMemoria

            if( quantidadePosicoesOcupadasMemoria + tamanhoProcesso >= tamanhoMaxMemoria ):
                self._removerProcessoMemoriaPrimaria( memoriaPrimaria, processo )

            posicaoInicial = self._mapaBits.indiceMemoriaLivre
            
            memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial )

            segmento = Segmento()
            segmento.processo = processo
            segmento.posicaoInicial = posicaoInicial
            segmento.quantidadePosicoes = tamanhoProcesso

            self._mapaBits.adicionarSegmento( segmento )
    '''

    def adicionarProcessoMemoriaPrimaria( self, memoriaPrimaria, processo = None ):
        
        if( processo == None ):
            self._removerProcessoMemoriaPrimaria( memoriaPrimaria, processo )

        else:
            quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )
            if( self._tamanhoPagina == None ):
                self._tamanhoPagina = processo.tamanhoProcesso

            tamanhoMaxMemoria = memoriaPrimaria.tamanhoMemoria

            if( quantidadePosicoesOcupadasMemoria + self._tamanhoPagina >= tamanhoMaxMemoria ):
                self._removerProcessoMemoriaPrimaria( memoriaPrimaria, processo )

            posicaoInicial = self._mapaBits.indiceMemoriaLivre
            
            memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial )

            segmento = Segmento()
            segmento.processo = processo
            segmento.posicaoInicial = posicaoInicial
            segmento.quantidadePosicoes = self._tamanhoPagina

            self._mapaBits.adicionarSegmento( segmento )


    
    def exibirMapaBits( self ):
        self._mapaBits.exibirMapaBits()

    def _removerProcessoMemoriaPrimaria( self, memoriaPrimaria, processo ):

        if( processo == None ):
            processoRemovido = memoriaPrimaria.liberarMemoria()

            self._mapaBits.removerSegmento()
            
            tempoVidaProcessoRemovido = processoRemovido.tempoVida

            if( tempoVidaProcessoRemovido > 0 ):
                MemoriaSecundaria.armazenarProcesso( processoRemovido )

        else:
            quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )
            tamanhoProcesso = processo.tamanhoProcesso
            tamanhoMaxMemoria = memoriaPrimaria.tamanhoMemoria

            while( quantidadePosicoesOcupadasMemoria + tamanhoProcesso >= tamanhoMaxMemoria ):
                processoRemovido = memoriaPrimaria.liberarMemoria()

                self._mapaBits.removerSegmento()
                
                tempoVidaProcessoRemovido = processoRemovido.tempoVida

                if( tempoVidaProcessoRemovido > 0 ):
                    MemoriaSecundaria.armazenarProcesso( processoRemovido )

                quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )  


    def _criarPagina( self, processo ):
        pass

    @property
    def tamanhoPagina( self ):
        return self._tamanhoPagina

    @tamanhoPagina.setter
    def tamanhoPagina( self, tamanhoPagina ):
        self._tamanhoPagina = tamanhoPagina
