#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#memoriaPrimariaTest.py

from memoriaSecundaria import MemoriaSecundaria
from memoriaPrimaria import MemoriaPrimaria
from segmento import Segmento
from mapeamentoEncadeadoBits import MapeamentoEncadeadoBits


class MemoriaPrimariaTest:

    @staticmethod
    def adicionarProcessoMemoria1ProcessoTamanhoTotalProcessoTest():
        print("\nadicionarProcessoMemoria1ProcessoTamanhoTotalProcessoTest")
        # Configuração
        caminhoDisco = "discorepositorio.csv"
        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )

        # Execução
        memoriaPrimaria = MemoriaPrimaria()
        posicaoInicial = 0
        memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial)

        # Validação
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoTotalProcesso()
    
    @staticmethod
    def adicionarProcessoMemoria2ProcessosTamanhoTotalProcessoTest():
        print("\nadicionarProcessoMemoria2ProcessosTamanhoTotalProcessoTest")
        # Configuração
        caminhoDisco = "discorepositorio.csv"
        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        processo1 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )

        # Execução
        memoriaPrimaria = MemoriaPrimaria()

        posicaoInicial = 0
        memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial )

        posicaoInicial = processo.tamanhoProcesso
        memoriaPrimaria.adicionarProcessoMemoria( processo1, posicaoInicial )

        # Validação
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoTotalProcesso()

    @staticmethod
    def adicionarProcessoMemoria3ProcessosTamanhoTotalProcessoTest():
        print("\nadicionarProcessoMemoria3ProcessosTamanhoTotalProcessoTest")
        # Configuração
        caminhoDisco = "discorepositorio.csv"
        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        processo1 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        processo2 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )

        # Execução
        memoriaPrimaria = MemoriaPrimaria()

        posicaoInicial = 0
        memoriaPrimaria.adicionarProcessoMemoria( processo, 0)

        posicaoInicial = processo.tamanhoProcesso
        memoriaPrimaria.adicionarProcessoMemoria( processo1, posicaoInicial)

        posicaoInicial = processo1.tamanhoProcesso
        memoriaPrimaria.adicionarProcessoMemoria( processo2, posicaoInicial)

        # Validação
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoTotalProcesso()

    @staticmethod
    def adicionarProcessoMemoria1ProcessoTamanhoPaginaTest():
        print("\nadicionarProcessoMemoria1ProcessoTamanhoPaginaTest")
        # Configuração
        caminhoDisco = "discorepositorio.csv"
        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        tamanhoPagina = 200

        # Execução
        memoriaPrimaria = MemoriaPrimaria()
        posicaoInicial = 0
        memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial, tamanhoPagina)

        # Validação
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoPagina(tamanhoPagina)
    
    @staticmethod
    def adicionarProcessoMemoria2ProcessosTamanhoPaginaTest():
        print("\nadicionarProcessoMemoria2ProcessosTamanhoPaginaTest")
        # Configuração
        caminhoDisco = "discorepositorio.csv"
        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        processo1 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        tamanhoPagina = 300

        # Execução
        memoriaPrimaria = MemoriaPrimaria()

        posicaoInicial = 0
        memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial, tamanhoPagina )

        posicaoInicial = tamanhoPagina
        memoriaPrimaria.adicionarProcessoMemoria( processo1, posicaoInicial, tamanhoPagina )

        # Validação
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoPagina(tamanhoPagina)

    @staticmethod
    def adicionarProcessoMemoria3ProcessosTamanhoPaginaTest():
        print("\nadicionarProcessoMemoria3ProcessosTamanhoPaginaTest")
        # Configuração
        caminhoDisco = "discorepositorio.csv"
        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        processo1 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        processo2 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        tamanhoPagina = 22

        # Execução
        memoriaPrimaria = MemoriaPrimaria()

        posicaoInicial = 0
        memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial, tamanhoPagina )

        posicaoInicial = tamanhoPagina
        memoriaPrimaria.adicionarProcessoMemoria( processo1, posicaoInicial, tamanhoPagina )

        posicaoInicial = tamanhoPagina
        memoriaPrimaria.adicionarProcessoMemoria( processo2, posicaoInicial, tamanhoPagina )

        # Validação
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoPagina(tamanhoPagina)

    @staticmethod
    def liberarMemoria3ProcessosIndice1TamanhoTotalProcessoTest():
        print("\nliberarMemoria3ProcessosIndice1TamanhoTotalProcessoTest")
        # Configuração
        memoriaPrimaria = MemoriaPrimaria()
        mapaBits = MapeamentoEncadeadoBits()
        caminhoDisco = "discorepositorio.csv"        

        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        posicaoInicial = mapaBits.indiceMemoriaLivre
        memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial )

        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = posicaoInicial
        segmento.quantidadePosicoes = processo.tamanhoProcesso

        mapaBits.adicionarSegmento( segmento )

        processo1 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        posicaoInicial = mapaBits.indiceMemoriaLivre
        memoriaPrimaria.adicionarProcessoMemoria( processo1, posicaoInicial )

        segmento1 = Segmento()
        segmento1.processo = processo1
        segmento1.posicaoInicial = posicaoInicial
        segmento1.quantidadePosicoes = processo1.tamanhoProcesso

        mapaBits.adicionarSegmento( segmento1 )        

        processo2 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        posicaoInicial = mapaBits.indiceMemoriaLivre
        memoriaPrimaria.adicionarProcessoMemoria( processo2, posicaoInicial )

        segmento2 = Segmento()
        segmento2.processo = processo2
        segmento2.posicaoInicial = posicaoInicial
        segmento2.quantidadePosicoes = processo2.tamanhoProcesso

        mapaBits.adicionarSegmento( segmento2 )

        # Execução
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoTotalProcesso()

        # OBSERVAR RETORNO DO -1 PARA BUSCA DA CLASSE
        indiceProcessoASerRemovido = mapaBits.buscarPosicaoInicialProcessoPelaClasseSubstituicao(0)
        memoriaPrimaria.liberarMemoria( indiceProcessoASerRemovido )

        # Validação
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoTotalProcesso()

    @staticmethod
    def liberarMemoria3ProcessosIndice1TamanhoPaginaTest():
        print("\nliberarMemoria3ProcessosIndice1TamanhoPaginaTest")
        # Configuração
        memoriaPrimaria = MemoriaPrimaria()
        mapaBits = MapeamentoEncadeadoBits()
        caminhoDisco = "discorepositorio.csv"
        tamanhoPagina = 20  

        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        processo.bitR = 1
        processo.bitM = 0
        posicaoInicial = mapaBits.indiceMemoriaLivre
        memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicial, tamanhoPagina )

        segmento = Segmento()
        segmento.processo = processo
        segmento.posicaoInicial = posicaoInicial
        segmento.quantidadePosicoes = tamanhoPagina
        segmento.definirClasseSubstituicaoPagina()

        mapaBits.adicionarSegmento( segmento )

        processo1 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        processo1.bitR = 0
        processo1.bitM = 0
        posicaoInicial = mapaBits.indiceMemoriaLivre
        memoriaPrimaria.adicionarProcessoMemoria( processo1, posicaoInicial, tamanhoPagina )

        segmento1 = Segmento()
        segmento1.processo = processo1
        segmento1.posicaoInicial = posicaoInicial
        segmento1.quantidadePosicoes = tamanhoPagina
        segmento1.definirClasseSubstituicaoPagina()

        mapaBits.adicionarSegmento( segmento1 )        

        processo2 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        processo2.bitR = 0
        processo2.bitM = 1
        posicaoInicial = mapaBits.indiceMemoriaLivre
        memoriaPrimaria.adicionarProcessoMemoria( processo2, posicaoInicial, tamanhoPagina )

        segmento2 = Segmento()
        segmento2.processo = processo2
        segmento2.posicaoInicial = posicaoInicial
        segmento2.quantidadePosicoes = tamanhoPagina
        segmento2.definirClasseSubstituicaoPagina()

        mapaBits.adicionarSegmento( segmento2 )

        # Execução
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoPagina(tamanhoPagina)
        indiceProcessoASerRemovido = mapaBits.buscarPosicaoInicialProcessoPelaClasseSubstituicao(0)
        memoriaPrimaria.liberarMemoria( indiceProcessoASerRemovido, tamanhoPagina )

        # Validação
        memoriaPrimaria.exibirMemoriaPrimariaTamanhoPagina(tamanhoPagina)

