#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#memoriaSecundariaTest.py

from memoriaSecundaria import MemoriaSecundaria
from processo import Processo

class MemoriaSecundariaTest:

    @staticmethod
    def buscarProcessoDiscoTest():
        #Configuração
        caminhoDisco = "discorepositorio.csv"

        # Execuação
        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )

        # Validação
        processo.exibirInfoProcesso()

    @staticmethod
    def buscaProcessoNivelAltoPrioridadeDiscoTest():
        # Configuração
        disco = open( "discorepositorio.csv", "r" )
        processosStr = disco.readlines()
        disco.close()

        memoriaSecundaria = MemoriaSecundaria()
        
        # Execução

        indice = memoriaSecundaria._buscaProcessoNivelAltoPrioridadeDisco( processosStr )

        # Validação
        print( indice )

