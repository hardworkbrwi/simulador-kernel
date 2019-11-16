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
            
            memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial, self._tamanhoPagina )

            segmento = Segmento()
            segmento.processo = processo
            segmento.posicaoInicial = posicaoInicial
            segmento.quantidadePosicoes = self._tamanhoPagina

            self._mapaBits.adicionarSegmento( segmento )


    

    def _removerProcessoMemoriaPrimaria( self, memoriaPrimaria, processo ):

        if( processo == None ):
            processoRemovido = memoriaPrimaria.liberarMemoria( self._tamanhoPagina )

            self._mapaBits.removerSegmento()
            
            #tempoVidaProcessoRemovido = processoRemovido.tempoVida

            # QUEM FARÁ ESSE CONTROLE SERÁ O KERNEL
            #if( tempoVidaProcessoRemovido > 0 ):
            #    MemoriaSecundaria.armazenarProcesso( processoRemovido )

        else:
            quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )
            tamanhoProcesso = processo.tamanhoProcesso
            tamanhoMaxMemoria = memoriaPrimaria.tamanhoMemoria

            while( quantidadePosicoesOcupadasMemoria + tamanhoProcesso >= tamanhoMaxMemoria ):
                processoRemovido = memoriaPrimaria.liberarMemoria()

                self._mapaBits.removerSegmento()
                
                tempoVidaProcessoRemovido = processoRemovido.tempoVida

                if( tempoVidaProcessoRemovido > 0 ):
                    MemoriaSecundaria.armazenarProcessoDisco( processoRemovido )

                quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )  


    def buscarProcessoASerRemovido( self, memoriaPrimaria ):
        '''
        Método de busca de processo a ser removido a partir de algorítimo de substituição de
        página LRU
        
        :int tempoVida:
        :field tempoVida: define o tempo de vida útil do processo
        '''
        indiceSegmento = -1
        processoASerRemovido = None
        for i in range( 0, 4 ):
            indiceSegmento = self._mapaBits.buscarSegmentoPorClasseSubstiuticao( i )
            if( indiceSegmento != -1 ):
                segmentoProcessoASerRemovido = self._mapaBits[indiceSegmento]
                processoASerRemovido = segmentoProcessoASerRemovido.processo

        return processoASerRemovido



    
    def exibirMapaBits( self ):
        self._mapaBits.exibirMapaBits()

    @property
    def tamanhoPagina( self ):
        return self._tamanhoPagina

    @tamanhoPagina.setter
    def tamanhoPagina( self, tamanhoPagina ):
        self._tamanhoPagina = tamanhoPagina
