#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#memoriaPrimariaTest.py

from memoriaSecundaria import MemoriaSecundaria
from memoriaPrimaria import MemoriaPrimaria

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

