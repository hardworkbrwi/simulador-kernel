#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#gerenciadorMemoriaTest.py

from random import randint

from processo import Processo
from segmento import Segmento
from memoriaPrimaria import MemoriaPrimaria
from mapeamentoEncadeadoBits import MapeamentoEncadeadoBits
from gerenciadorMemoria import GerenciadorMemoria
from memoriaSecundaria import MemoriaSecundaria


class GerenciadorMemoriaTest:

    @classmethod
    def geradorDeProcessos( cls ):
        listaProcessos = []
        for id in range( 5 ):
            processo = Processo()
            processo.idProcesso = id
            processo.tamanhoProcesso = randint( 200, 400 )
            processo.prioridade = randint( 0, 4 )
            processo.tempoVida = randint( 2, 20 )
            processo.bitR = randint( 0, 1 )
            processo.bitM = randint( 0, 1 )

            listaProcessos.append( processo )

        return listaProcessos

    @classmethod
    def geradorDeMapaBits( cls, listaProcessos, tamanhoPagina = None ):
        mapaBits = MapeamentoEncadeadoBits()        

        for processo in listaProcessos:
            posicaoInicial = mapaBits.indiceMemoriaLivre

            segmento = Segmento()
            segmento.processo = processo
            segmento.posicaoInicial = posicaoInicial
            if( tamanhoPagina != None ):
                segmento.quantidadePosicoes = tamanhoPagina
            else:
                segmento.quantidadePosicoes = processo.tamanhoProcesso

            mapaBits.adicionarSegmento( segmento )

        return mapaBits

    @staticmethod
    def adicionar1ProcessoMemoriaPrimariaTamanhoProcessoTest():
        print("\nadicionar1ProcessoMemoriaPrimariaTamanhoProcessoTest")
        # Configuração        
        listaProcessos = GerenciadorMemoriaTest.geradorDeProcessos()

        memoriaPrimaria = MemoriaPrimaria()

        # Execução
        gerenciadorMemoria = GerenciadorMemoria()
        gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, listaProcessos[0] )

        # Validação
        listaProcessos[0].exibirInfoProcesso()
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoTotalProcesso()
        gerenciadorMemoria.exibirMapaBits()

    @staticmethod
    def adicionar3ProcessoMemoriaPrimariaTamanhoProcessoTest():
        print("\nadicionar3ProcessoMemoriaPrimariaTamanhoProcessoTest")
        # Configuração        
        listaProcessos = GerenciadorMemoriaTest.geradorDeProcessos()

        memoriaPrimaria = MemoriaPrimaria()

        # Execução
        gerenciadorMemoria = GerenciadorMemoria()
        for i in range( 3 ):
            gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, listaProcessos[i] )

        # Validação
        for i in range( 3 ):
            listaProcessos[i].exibirInfoProcesso()
        
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoTotalProcesso()
        gerenciadorMemoria.exibirMapaBits()

    @staticmethod
    def adicionar1ProcessoMemoriaPrimariaTamanhoPaginaTest():
        print("\nadicionar1ProcessoMemoriaPrimariaTamanhoPaginaTest")
        # Configuração        
        listaProcessos = GerenciadorMemoriaTest.geradorDeProcessos()

        memoriaPrimaria = MemoriaPrimaria()


        # Execução
        gerenciadorMemoria = GerenciadorMemoria()
        gerenciadorMemoria.tamanhoPagina = 25
        gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, listaProcessos[0] )

        # Validação
        listaProcessos[0].exibirInfoProcesso()
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoPagina(gerenciadorMemoria.tamanhoPagina)
        gerenciadorMemoria.exibirMapaBits()

    @staticmethod
    def adicionar3ProcessoMemoriaPrimariaTamanhoPaginaTest():
        print("\nadicionar3ProcessoMemoriaPrimariaTamanhoPaginaTest")
        # Configuração        
        listaProcessos = GerenciadorMemoriaTest.geradorDeProcessos()

        memoriaPrimaria = MemoriaPrimaria()


        # Execução
        gerenciadorMemoria = GerenciadorMemoria()
        gerenciadorMemoria.tamanhoPagina = 25
        for i in range( 3 ):
            gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, listaProcessos[i] )

        # Validação
        for i in range( 3 ):
            listaProcessos[i].exibirInfoProcesso()
        
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoPagina(gerenciadorMemoria.tamanhoPagina)
        gerenciadorMemoria.exibirMapaBits()

    @staticmethod
    def liberarEspacoMemoriaPrimariaTest():
        print("\nliberarEspacoMemoriaPrimariaTest")
        # Configuração   
        listaProcessos = GerenciadorMemoriaTest.geradorDeProcessos()

        memoriaPrimaria = MemoriaPrimaria()

         # Execução
        gerenciadorMemoria = GerenciadorMemoria()
        for i in range( 5 ):
            gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, listaProcessos[i] )

        for i in range( 5 ):
            listaProcessos[i].exibirInfoProcesso()
        
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoTotalProcesso()
        gerenciadorMemoria.exibirMapaBits()

        espacoASerliberado = 1000

        # Validação
        listaProcessos = gerenciadorMemoria.liberarEspacoMemoriaPrimaria( memoriaPrimaria, espacoASerliberado )
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoTotalProcesso()
        gerenciadorMemoria.exibirMapaBits()

        if( len( listaProcessos ) != 0 ):
            print( "Há {} processos.".format( len(listaProcessos) ) )
            for processo in listaProcessos:
                processo.exibirInfoProcesso()
        else:
            print( "A lista de processos está vazia." )


    
    @staticmethod
    def buscarPaginaASerRemovidaPorClasseTest():
        print("\nbuscarPaginaASerRemovidaPorClasseTest")
        # Configuração
        gerenciadorMemoria = GerenciadorMemoria()
        
        listaProcessos = GerenciadorMemoriaTest.geradorDeProcessos()
        mapaBits = GerenciadorMemoriaTest.geradorDeMapaBits( listaProcessos )

        # Execução
        gerenciadorMemoria = GerenciadorMemoria()
        mapaBits.atualizarClassesSubstituicaoPagina()
        #mapaBits.exibirMapaBits()
        gerenciadorMemoria.exibirMapaBits()
        
        for processo in listaProcessos:
            processo.exibirInfoProcesso()

        indiceSegmentoASerRemovido = gerenciadorMemoria._buscarPaginaASerRemovidaPorClasse()

        # Validação
        print(indiceSegmentoASerRemovido)