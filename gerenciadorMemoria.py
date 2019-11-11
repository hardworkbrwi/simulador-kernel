#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#gerenciadorMemoria.py

from mapeamentoEncadeadoBits import MapeamentoEncadeadoBits
from segmento import Segmento
from memoriaSecundaria import MemoriaSecundaria

class GerenciadorMemoria:

    """ Description	"""
    
    __slots__ = [ "_mapaBits" ]

    def __init__( self ):
        self._mapaBits = MapeamentoEncadeadoBits()

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
            
            memoriaPrimaria.executarProcessoMemoria( processo, posicaoInicial )

            segmento = Segmento()
            segmento.processo = processo
            segmento.posicaoInicial = posicaoInicial
            segmento.quantidadePosicoes = tamanhoProcesso

            self._mapaBits.adicionarSegmento( segmento )

    def adicionarPaginaMemoriaPrimaria( self, memoriaPrimaria, processo = None ):
        pass
    
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
