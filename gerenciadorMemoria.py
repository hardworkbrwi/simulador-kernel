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

    def adicionarProcessoMemoriaPrimaria( self, memoriaPrimaria, processo, tamanhoPagina = None ):

        # Retorna falsa se não há processo no disco
        # Se existe processo no disco verdadeiro
        quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )
        tamanhoMaxMemoria = memoriaPrimaria.tamanhoMemoria

        if( tamanhoPagina == None ):
            espacoOcupadoProcesso = processo.tamanhoProcesso
        else:
            espacoOcupadoProcesso = tamanhoPagina

        if( quantidadePosicoesOcupadasMemoria + espacoOcupadoProcesso > tamanhoMaxMemoria ):
            self._liberarEspacoMemoriaPrimaria( memoriaPrimaria, espacoOcupadoProcesso )
        '''
            # REMOVER USANDO ALGORÍTIMO DE SUBSTITUIÇÃO DE PÁGINA LRU
            while( quantidadePosicoesOcupadasMemoria + espacoOcupadoProcesso > tamanhoMaxMemoria ):

                indicePosicaoInicialProcessoASerRemovidoMemoria = self._buscarPaginaASerRemovidaPorClasse()
                if( indicePosicaoInicialProcessoASerRemovidoMemoria != -1 ):
                    idProcessoASerRemovido = memoriaPrimaria.posicoesMemoria[ indicePosicaoInicialProcessoASerRemovidoMemoria ]

                    memoriaPrimaria.liberarMemoria( indicePosicaoInicialProcessoASerRemovidoMemoria, espacoOcupadoProcesso )
                
                    indiceSegmentoASerRemovido = self._mapaBits.buscarIndiceSegmentoPorIdProcesso( idProcessoASerRemovido )
                    self._mapaBits.removerSegmento( indiceSegmentoASerRemovido )

                    quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )

                else:
                    print( "Não foram encontradas paginas com classes de substituição definidas." )

            # Fim de remover segmento
        '''

        posicaoInicial = self._mapaBits.indiceMemoriaLivre
        memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial, espacoOcupadoProcesso)

        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = posicaoInicial
        segmento.quantidadePosicoes = espacoOcupadoProcesso

        self._mapaBits.adicionarSegmento( segmento )

    def _liberarEspacoMemoriaPrimaria( self, memoriaPrimaria, espacoASerLiberado ):
        listaProcessosRemovidos = []
        quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )
        tamanhoMaxMemoria = memoriaPrimaria.tamanhoMemoria

        # REMOVER USANDO ALGORÍTIMO DE SUBSTITUIÇÃO DE PÁGINA LRU
        while( quantidadePosicoesOcupadasMemoria + espacoASerLiberado > tamanhoMaxMemoria ):

            indicePosicaoInicialProcessoASerRemovidoMemoria = self._buscarPaginaASerRemovidaPorClasse()
            if( indicePosicaoInicialProcessoASerRemovidoMemoria != -1 ):
                idProcessoASerRemovido = memoriaPrimaria.posicoesMemoria[ indicePosicaoInicialProcessoASerRemovidoMemoria ]

                processoRemovido = memoriaPrimaria.liberarMemoria( indicePosicaoInicialProcessoASerRemovidoMemoria, espacoASerLiberado )
                listaProcessosRemovidos.append( processoRemovido )
            
                indiceSegmentoASerRemovido = self._mapaBits.buscarIndiceSegmentoPorIdProcesso( idProcessoASerRemovido )
                self._mapaBits.removerSegmento( indiceSegmentoASerRemovido )

                quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )

            else:
                print( "Não foram encontradas paginas com classes de substituição definidas." )
            
        return listaProcessosRemovidos

        # Fim de remover segmento





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
    

    '''
    def _removerProcessoMemoriaPrimaria( self, memoriaPrimaria, processo, tamanhoPagina ):

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

    # Obsoleto
    def buscarProcessoASerRemovido( self, memoriaPrimaria ):
    
        Método de busca de processo a ser removido a partir de algorítimo de substituição de
        página LRU
        
        :int tempoVida:
        :field tempoVida: define o tempo de vida útil do processo

        indiceSegmento = -1
        processoASerRemovido = None
        for i in range( 0, 4 ):
            indiceSegmento = self._mapaBits.buscarSegmentoPorClasseSubstiuticao( i )
            if( indiceSegmento != -1 ):
                segmentoProcessoASerRemovido = self._mapaBits[indiceSegmento]
                processoASerRemovido = segmentoProcessoASerRemovido.processo

        return processoASerRemovido
    '''



    
    def exibirMapaBits( self ):
        self._mapaBits.exibirMapaBits()

    @property
    def tamanhoPagina( self ):
        return self._tamanhoPagina

    @tamanhoPagina.setter
    def tamanhoPagina( self, tamanhoPagina ):
        self._tamanhoPagina = tamanhoPagina
