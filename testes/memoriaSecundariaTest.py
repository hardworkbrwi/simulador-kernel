#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#memoriaSecundariaTest.py

from memoriaSecundaria import MemoriaSecundaria
from processo import Processo

class MemoriaSecundariaTest:

    @staticmethod
    def buscarProcessoDiscoTest():
        print("\nbuscarProcessoDiscoTest")
        #Configuração
        caminhoDisco = "discorepositorio.csv"

        # Execuação
        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )

        # Validação
        processo.exibirInfoProcesso()

    @staticmethod
    def buscarProcessoNivelAltoPrioridadeDiscoTest():
        print("\nbuscaProcessoNivelAltoPrioridadeDiscoTest")
        # Configuração
        disco = open( "discorepositorio.csv", "r" )
        processosStr = disco.readlines()
        disco.close()

        memoriaSecundaria = MemoriaSecundaria()
        
        # Execução

        indice = memoriaSecundaria._buscarProcessoNivelAltoPrioridadeDisco( processosStr )

        # Validação
        print( indice )

    @staticmethod
    def armazenarProcessoDiscoTest():
        print("\narmazenarProcessoDiscoTest")
        # Configuração
        caminhoDisco = "discorepositorio.csv"

        processo = Processo()
        processo.idProcesso = 380
        processo.tamanhoProcesso = 560
        processo.tempoVida = 30
        
        # Execução
        MemoriaSecundaria.armazenarProcessoDisco( processo, caminhoDisco )

        disco = open( "discorepositorio.csv", "r" )
        processosStr = disco.readlines()
        disco.close()

        # Validação
        print(processosStr[-1])



