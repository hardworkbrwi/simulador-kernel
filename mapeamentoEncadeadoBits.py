#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#mapeamentoEncadeadoBits.py

class MapeamentoEncadeadoBits:
    """
    Define o objeto de Mapa de bits para poder diponibilizar informações ao
    gerenciador de memória.

    :List<Segmento> listaSegmento
    :param listaSegmento: lista de segmentos do mapa de bits

    :int indiceMemoriaLivre
    :param indiceMemoriaLivre: indice do próximo segmento livre
    """
    __slots__ = [ "_listaSegmentos", "_indiceMemoriaLivre" ]

    def __init__( self ):
        self._listaSegmentos = []
        self._indiceMemoriaLivre = 0

    def adicionarSegmento( self, segmento ):
    
        """ Description
        :Segmento segmento:
        :param segmento:
    
        :raises:
    
        :rtype:
        """
        self._listaSegmentos.append( segmento )
        
        quantidadePosicoes = segmento.quantidadePosicoes
        self._atualizarIndiceMemoriaLivre( True, quantidadePosicoes )

    def removerSegmento( self ):
        segmentoEliminado = self._listaSegmentos.pop(0)

        quantidadePosicoes = segmentoEliminado.quantidadePosicoes

        self._atualizarIndiceInicialSegmento( quantidadePosicoes )
        self._atualizarIndiceMemoriaLivre( False, quantidadePosicoes )

    def buscarSegmentoPorClasseSubstiuticao( self, classeSubstituicao ):
        segmentoEncontrado = -1
        for indice, segmento in enumerate( self._listaSegmentos ):
            if( segmento.classeSubstituicao == classeSubstituicao ):
                return indice
        
        return segmentoEncontrado


    def exibirMapaBits( self ):
        """
		Exibe a lista de segmentos do mapara de bits
		"""
        print( "-------- MAPA DE BITS --------".center(62) )
        LINHA = "-"
        grade = 62 * LINHA
        print( grade )
        print( "{}|{}|{}|{}".format( "ID PROCESSO".center(12),
                                     "POSIÇÃO INICIAL".center(16),
                                     "QUANTIDADE POSICÕES".center(19),
                                     "TEMPO DE VIDA".center(14) ) )
        print( grade )
        for segmento in self._listaSegmentos:
            print( "{}|{}|{}|{}".format( str(segmento.processo.idProcesso).ljust(12),
                                      str(segmento.posicaoInicial).ljust(16),
                                      str(segmento.quantidadePosicoes).ljust(19),
                                      str(segmento.processo.tempoVida).ljust(14) ) )
        print( grade )
        print( "Próximo indice de memória livre: posicão - {}\n".format( self.indiceMemoriaLivre ) )

    def _atualizarIndiceInicialSegmento( self, quantidadePosicoes ):
        quantidadeElementos = len( self._listaSegmentos )
        for i in range( 0,  quantidadeElementos ):
            self._listaSegmentos[i].posicaoInicial -= quantidadePosicoes

    def _atualizarIndiceMemoriaLivre( self, segmentoAdicionado, quantidadePosicoes ):
        if( segmentoAdicionado ):
            self._indiceMemoriaLivre += quantidadePosicoes

        else:
            self._indiceMemoriaLivre -= quantidadePosicoes

    @property
    def indiceMemoriaLivre( self ):
        return self._indiceMemoriaLivre


