#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#segmentoTest.py

from processo import Processo
from segmento import Segmento
from mapeamentoEncadeadoBits import MapeamentoEncadeadoBits

class MapeamentoEncadeadoBitsTest:

    @classmethod
    def popularMapaBits( cls, listaTamanhoProcesso ):
        processo = Processo()
        processo.bitR = 0
        processo.bitM = 0
        processo.tamanhoProcesso = listaTamanhoProcesso[0]

        processo1 = Processo()
        processo1.bitR = 0
        processo1.bitM = 0
        processo1.tamanhoProcesso = listaTamanhoProcesso[1]

        processo2 = Processo()
        processo2.bitR = 0
        processo2.bitM = 1
        processo2.tamanhoProcesso = listaTamanhoProcesso[2]

        processo3 = Processo()
        processo3.bitR = 1
        processo3.bitM = 1
        processo3.tamanhoProcesso = listaTamanhoProcesso[3]

        processo4 = Processo()
        processo4.bitR = 1
        processo4.bitM = 0
        processo4.tamanhoProcesso = listaTamanhoProcesso[4]

        mapeamentoEncadeadoBits = MapeamentoEncadeadoBits()

        segmento = Segmento()
        segmento.processo = processo
        segmento.definirClasseSubstituicaoPagina()
        segmento.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento.quantidadePosicoes = processo.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento )

        segmento1 = Segmento()
        segmento1.processo = processo1
        segmento1.definirClasseSubstituicaoPagina()
        segmento1.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento1.quantidadePosicoes = processo1.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento1 )

        segmento2 = Segmento()
        segmento2.processo = processo2
        segmento2.definirClasseSubstituicaoPagina()
        segmento2.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento2.quantidadePosicoes = processo2.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento2 )

        segmento3 = Segmento()
        segmento3.processo = processo3
        segmento3.definirClasseSubstituicaoPagina()
        segmento3.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento3.quantidadePosicoes = processo3.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento3 )

        segmento4 = Segmento()
        segmento4.processo = processo4
        segmento4.definirClasseSubstituicaoPagina()
        segmento4.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento4.quantidadePosicoes = processo4.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento4 )

        return mapeamentoEncadeadoBits

    @staticmethod
    def adicionarSegmentoTest():
        print( "\nadicionarSegmentoTest" )
        # Configuração
        processo = Processo()
        processo.tamanhoProcesso = 255

        mapeamentoEncadeadoBits = MapeamentoEncadeadoBits()

        # Execução
        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento.quantidadePosicoes = processo.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento )

        # Validação
        mapeamentoEncadeadoBits.exibirMapaBits()

    @staticmethod
    def adicionarSegmentoVericarIndiceMemoriaLivreAtualizadoTest():
        print( "\nadicionarSegmentoVericarIndiceMemoriaLivreAtualizadoTest" )
        # Configuração
        processo = Processo()
        processo.tamanhoProcesso = 255

        processo1 = Processo()
        processo1.tamanhoProcesso = 350

        processo2 = Processo()
        processo2.tamanhoProcesso = 500

        mapeamentoEncadeadoBits = MapeamentoEncadeadoBits()

        # Execução
        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento.quantidadePosicoes = processo.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento )

        segmento1 = Segmento()
        segmento1.processo = processo1
        segmento1.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento1.quantidadePosicoes = processo1.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento1 )

        segmento2 = Segmento()
        segmento2.processo = processo2
        segmento2.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento2.quantidadePosicoes = processo2.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento2 )

        # Validação
        mapeamentoEncadeadoBits.exibirMapaBits()

    @staticmethod
    def adicionarSegmentoTamanhoProcessoTest():
        print("adicionarSegmentoTamanhoProcessoTest")
        # Configuração
        processo = Processo()
        processo.tamanhoProcesso = 150

        processo1 = Processo()
        processo1.tamanhoProcesso = 120

        processo2 = Processo()
        processo2.tamanhoProcesso = 300

        mapeamentoEncadeadoBits = MapeamentoEncadeadoBits()

        # Execução
        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento.quantidadePosicoes = processo.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento )

        segmento1 = Segmento()
        segmento1.processo = processo1
        segmento1.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento1.quantidadePosicoes = processo1.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento1 )
        
        segmento2 = Segmento()
        segmento2.processo = processo2
        segmento2.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento2.quantidadePosicoes = processo2.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento2 )

        # Validação
        mapeamentoEncadeadoBits.exibirMapaBits()

    @staticmethod
    def adicionarSegmentoTamanhoPaginaTest():
        print("adicionarSegmentoTamanhoPaginaTest")
        # Configuração
        tamanhoPagina = 200
        processo = Processo()
        processo.tamanhoProcesso = 150

        processo1 = Processo()
        processo1.tamanhoProcesso = 120

        processo2 = Processo()
        processo2.tamanhoProcesso = 300

        mapeamentoEncadeadoBits = MapeamentoEncadeadoBits()

        # Execução
        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento.quantidadePosicoes = tamanhoPagina

        mapeamentoEncadeadoBits.adicionarSegmento( segmento )

        segmento1 = Segmento()
        segmento1.processo = processo1
        segmento1.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento1.quantidadePosicoes = tamanhoPagina

        mapeamentoEncadeadoBits.adicionarSegmento( segmento1 )

        segmento2 = Segmento()
        segmento2.processo = processo2
        segmento2.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento2.quantidadePosicoes = tamanhoPagina

        mapeamentoEncadeadoBits.adicionarSegmento( segmento2 )

        # Validação
        mapeamentoEncadeadoBits.exibirMapaBits()

    @staticmethod
    def removerSegmentoIndice0Test():
        print("\nremoverSegmentoIndice0Test")
        # Configuração
        processo = Processo()
        processo.tamanhoProcesso = 150

        processo1 = Processo()
        processo1.tamanhoProcesso = 120

        processo2 = Processo()
        processo2.tamanhoProcesso = 300

        processo3 = Processo()
        processo3.tamanhoProcesso = 650

        mapeamentoEncadeadoBits = MapeamentoEncadeadoBits()

        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento.quantidadePosicoes = processo.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento )

        segmento1 = Segmento()
        segmento1.processo = processo1
        segmento1.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento1.quantidadePosicoes = processo1.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento1 )

        segmento2 = Segmento()
        segmento2.processo = processo2
        segmento2.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento2.quantidadePosicoes = processo2.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento2 )

        segmento3 = Segmento()
        segmento3.processo = processo3
        segmento3.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento3.quantidadePosicoes = processo3.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento3 )

        # Execução
        mapeamentoEncadeadoBits.exibirMapaBits()
        mapeamentoEncadeadoBits.removerSegmento(0)

        # Validação
        mapeamentoEncadeadoBits.exibirMapaBits()

    @staticmethod
    def removerSegmentoIndice1Test():
        print("\nremoverSegmentoIndice1Test")
        # Configuração
        processo = Processo()
        processo.tamanhoProcesso = 150

        processo1 = Processo()
        processo1.tamanhoProcesso = 120

        processo2 = Processo()
        processo2.tamanhoProcesso = 300

        processo3 = Processo()
        processo3.tamanhoProcesso = 650

        mapeamentoEncadeadoBits = MapeamentoEncadeadoBits()

        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento.quantidadePosicoes = processo.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento )

        segmento1 = Segmento()
        segmento1.processo = processo1
        segmento1.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento1.quantidadePosicoes = processo1.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento1 )

        segmento2 = Segmento()
        segmento2.processo = processo2
        segmento2.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento2.quantidadePosicoes = processo2.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento2 )

        segmento3 = Segmento()
        segmento3.processo = processo3
        segmento3.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento3.quantidadePosicoes = processo3.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento3 )

        # Execução
        mapeamentoEncadeadoBits.exibirMapaBits()
        mapeamentoEncadeadoBits.removerSegmento(1)

        # Validação
        mapeamentoEncadeadoBits.exibirMapaBits()

    @staticmethod
    def removerSegmentoIndice2Test():
        print("\nremoverSegmentoIndice2Test")
        # Configuração
        processo = Processo()
        processo.tamanhoProcesso = 150

        processo1 = Processo()
        processo1.tamanhoProcesso = 120

        processo2 = Processo()
        processo2.tamanhoProcesso = 300

        processo3 = Processo()
        processo3.tamanhoProcesso = 650

        mapeamentoEncadeadoBits = MapeamentoEncadeadoBits()

        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento.quantidadePosicoes = processo.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento )

        segmento1 = Segmento()
        segmento1.processo = processo1
        segmento1.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento1.quantidadePosicoes = processo1.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento1 )

        segmento2 = Segmento()
        segmento2.processo = processo2
        segmento2.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento2.quantidadePosicoes = processo2.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento2 )

        segmento3 = Segmento()
        segmento3.processo = processo3
        segmento3.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento3.quantidadePosicoes = processo3.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento3 )

        # Execução
        mapeamentoEncadeadoBits.exibirMapaBits()
        mapeamentoEncadeadoBits.removerSegmento(2)

        # Validação
        mapeamentoEncadeadoBits.exibirMapaBits()

    @staticmethod
    def removerSegmentoIndice3Test():
        print("\nremoverSegmentoIndice3Test")
        # Configuração
        processo = Processo()
        processo.tamanhoProcesso = 150

        processo1 = Processo()
        processo1.tamanhoProcesso = 120

        processo2 = Processo()
        processo2.tamanhoProcesso = 300

        processo3 = Processo()
        processo3.tamanhoProcesso = 650

        mapeamentoEncadeadoBits = MapeamentoEncadeadoBits()

        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento.quantidadePosicoes = processo.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento )

        segmento1 = Segmento()
        segmento1.processo = processo1
        segmento1.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento1.quantidadePosicoes = processo1.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento1 )

        segmento2 = Segmento()
        segmento2.processo = processo2
        segmento2.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento2.quantidadePosicoes = processo2.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento2 )

        segmento3 = Segmento()
        segmento3.processo = processo3
        segmento3.posicaoInicial = mapeamentoEncadeadoBits.indiceMemoriaLivre
        segmento3.quantidadePosicoes = processo3.tamanhoProcesso

        mapeamentoEncadeadoBits.adicionarSegmento( segmento3 )

        # Execução
        mapeamentoEncadeadoBits.exibirMapaBits()
        mapeamentoEncadeadoBits.removerSegmento(3)

        # Validação
        mapeamentoEncadeadoBits.exibirMapaBits()

    @staticmethod
    def buscarSegmentoPorClasseSubstituicao0Test():
        print("\nbuscarSegmentoPorClasseSubstituicao0Test")
        # Configuração
        listaTamanhoProcesso = [ 150, 120, 300, 650, 150 ]
        mapabits = MapeamentoEncadeadoBitsTest.popularMapaBits( listaTamanhoProcesso )
        indiceClasse = 0

        # Execução
        indiceSegmento = mapabits.buscarSegmentoPorClasseSubstiuticao(indiceClasse)

        # Validação
        print( indiceSegmento )

    @staticmethod
    def buscarSegmentoPorClasseSubstituicao1Test():
        print("\nbuscarSegmentoPorClasseSubstituicao1Test")
        # Configuração
        listaTamanhoProcesso = [ 150, 120, 300, 650, 150 ]
        mapabits = MapeamentoEncadeadoBitsTest.popularMapaBits( listaTamanhoProcesso )
        indiceClasse = 1

        # Execução
        indiceSegmento = mapabits.buscarSegmentoPorClasseSubstiuticao(indiceClasse)

        # Validação
        print( indiceSegmento )

    @staticmethod
    def buscarSegmentoPorClasseSubstituicao2Test():
        print("\nbuscarSegmentoPorClasseSubstituicao2Test")
        # Configuração
        listaTamanhoProcesso = [ 150, 120, 300, 650, 150 ]
        mapabits = MapeamentoEncadeadoBitsTest.popularMapaBits( listaTamanhoProcesso )
        indiceClasse = 2

        # Execução
        indiceSegmento = mapabits.buscarSegmentoPorClasseSubstiuticao(indiceClasse)

        # Validação
        print( indiceSegmento )

    @staticmethod
    def buscarSegmentoPorClasseSubstituicao3Test():
        print("\nbuscarSegmentoPorClasseSubstituicao3Test")
        # Configuração
        listaTamanhoProcesso = [ 150, 120, 300, 650, 150 ]
        mapabits = MapeamentoEncadeadoBitsTest.popularMapaBits( listaTamanhoProcesso )
        indiceClasse = 3

        # Execução
        indiceSegmento = mapabits.buscarSegmentoPorClasseSubstiuticao(indiceClasse)

        # Validação
        print( indiceSegmento )

    @staticmethod
    def buscarSegmentoPorClasseSubstituicaoIndeterminadaTest():
        print("\nbuscarSegmentoPorClasseSubstituicaoIndeterminadaTest")
        # Configuração
        listaTamanhoProcesso = [ 150, 120, 300, 650, 150 ]
        mapabits = MapeamentoEncadeadoBitsTest.popularMapaBits( listaTamanhoProcesso )
        indiceClasse = 4

        # Execução
        indiceSegmento = mapabits.buscarSegmentoPorClasseSubstiuticao(indiceClasse)

        # Validação
        print( indiceSegmento )

        