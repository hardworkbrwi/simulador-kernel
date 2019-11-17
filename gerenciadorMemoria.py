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

    def adicionarProcessoMemoriaPrimaria( self, memoriaPrimaria, processo ):

        if( self._tamanhoPagina == None ):
            espacoOcupadoProcesso = processo.tamanhoProcesso
        else:
            espacoOcupadoProcesso = self._tamanhoPagina

        posicaoInicial = self._mapaBits.indiceMemoriaLivre
        memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial, espacoOcupadoProcesso )

        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = posicaoInicial
        segmento.quantidadePosicoes = espacoOcupadoProcesso

        self._mapaBits.adicionarSegmento( segmento )

    def liberarEspacoMemoriaPrimaria( self, memoriaPrimaria, espacoASerLiberado ):
        listaProcessosRemovidos = []
        quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )
        tamanhoMaxMemoria = memoriaPrimaria.tamanhoMemoria

        # REMOVER USANDO ALGORÍTIMO DE SUBSTITUIÇÃO DE PÁGINA LRU
        while( quantidadePosicoesOcupadasMemoria + espacoASerLiberado > tamanhoMaxMemoria ):

            indicePosicaoInicialProcessoASerRemovidoMemoria = self._buscarPaginaASerRemovidaPorClasse()
            if( indicePosicaoInicialProcessoASerRemovidoMemoria != -1 ):
                idProcessoASerRemovido = memoriaPrimaria.posicoesMemoria[ indicePosicaoInicialProcessoASerRemovidoMemoria ].idProcesso
                if( self._tamanhoPagina == None ):
                    tamanhoPaginaProcessoASerRemovido = memoriaPrimaria.posicoesMemoria[ indicePosicaoInicialProcessoASerRemovidoMemoria ].tamanhoProcesso
                else:
                    tamanhoPaginaProcessoASerRemovido = self._tamanhoPagina

                processoRemovido = memoriaPrimaria.liberarMemoria( indicePosicaoInicialProcessoASerRemovidoMemoria, tamanhoPaginaProcessoASerRemovido )
                listaProcessosRemovidos.append( processoRemovido )
            
                indiceSegmentoASerRemovido = self._mapaBits.buscarIndiceSegmentoPorIdProcesso( idProcessoASerRemovido )
                self._mapaBits.removerSegmento( indiceSegmentoASerRemovido )

                quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )

            else:
                print( "Não foram encontradas paginas com classes de substituição definidas." )
            
        return listaProcessosRemovidos

        # Fim de remover segmento

    def exibirMapaBits( self ):
        self._mapaBits.exibirMapaBits()
    
    def _buscarPaginaASerRemovidaPorClasse( self ):
        self._mapaBits.atualizarClassesSubstituicaoPagina()

        posicaoInicialProcessoBuscado = -1
        for i in range( 0, 3 ):
            posicaoInicialProcessoBuscado = self._mapaBits.buscarPosicaoInicialProcessoPelaClasseSubstituicao( i )
            if( posicaoInicialProcessoBuscado != -1 ):
                return posicaoInicialProcessoBuscado
        
        return posicaoInicialProcessoBuscado
    
    '''
    def adicionarProcessoMemoriaPrimaria( self, memoriaPrimaria, processo = None, tamanhoPagina = None ):

        # Retorna falsa se não há processo no disco
        # Se existe processo no disco verdadeiro
        
        if( processo == None ):
            self._removerProcessoMemoriaPrimaria( memoriaPrimaria, processo, tamanhoPagina )

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

    '''


    @property
    def tamanhoPagina( self ):
        return self._tamanhoPagina

    @tamanhoPagina.setter
    def tamanhoPagina( self, tamanhoPagina ):
        self._tamanhoPagina = tamanhoPagina
