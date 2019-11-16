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
    
        """ Função para adicionar segmento ao mapa de bits. Chama a função para 
        atualiza o índice de memória livre, a fim de informar o próximo espaço
        livre de memória disponível.

        :Segmento segmento:
        :param segmento: segmento a ser adicionado a lista
        """
        self._listaSegmentos.append( segmento )
        
        quantidadePosicoes = segmento.quantidadePosicoes
        self._atualizarIndiceMemoriaLivre( True, quantidadePosicoes )

    def removerSegmento( self, indiceASerRemovido ):
        segmentoEliminado = self._listaSegmentos.pop( indiceASerRemovido )

        quantidadePosicoes = segmentoEliminado.quantidadePosicoes

        self._atualizarIndiceInicialSegmento( quantidadePosicoes, indiceASerRemovido )
        self._atualizarIndiceMemoriaLivre( False, quantidadePosicoes )

    def buscarPosicaoInicialProcessoPelaClasseSubstituicao( self, indiceClasseSubstituicao ):
        posicaoInicialSegmentoEncontrado = -1
        for indice, segmento in enumerate( self._listaSegmentos ):
            if( segmento.classeSubstituicao == indiceClasseSubstituicao ):
                posicaoInicialSegmentoEncontrado = self._listaSegmentos[indice].posicaoInicial
                return posicaoInicialSegmentoEncontrado
        
        return posicaoInicialSegmentoEncontrado

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

    def _atualizarIndiceInicialSegmento( self, quantidadePosicoes, indiceInicialDecremento ):
        """ Função para atualizar o índice inicial de todos os segmentos a partir do indice inicial passado como parâremetro.

        :int quantidadePosicoes:
        :param quantidadePosicoes: quantidade de posições a serem decrementadas do atributo de posicaoInicial dos segmentos

        :int indiceInicialDecremento:
        :param indiceInicialDecremento: Indice ao qual deverá iniciar o decremento para atualização da posicaoInicial
        """
        quantidadeElementos = len( self._listaSegmentos )
        for i in range( indiceInicialDecremento,  quantidadeElementos ):
            self._listaSegmentos[i].posicaoInicial -= quantidadePosicoes

    def _atualizarIndiceMemoriaLivre( self, segmentoAdicionado, quantidadePosicoes ):
        """ Função para atualizar o índice de memória livre,
        a fim de informar o próximo espaço livre de memória disponível.

        :boolean segmentoAdicionado:
        :param segmentoAdicionado: se o parâmetro for True o segmento foi adicionado e
        o indiceMemoriaLivre deverá ser incrementado. Caso contrário o indiceMemoriaLivre
        será decrementado.

        :int quantidadePosicoes:
        :param quantidadePosicoes: quantidade de posições a ser incrementado ou decrementada
        no mapara de bits.
        """
        if( segmentoAdicionado ):
            self._indiceMemoriaLivre += quantidadePosicoes

        else:
            self._indiceMemoriaLivre -= quantidadePosicoes

    @property
    def indiceMemoriaLivre( self ):
        return self._indiceMemoriaLivre


