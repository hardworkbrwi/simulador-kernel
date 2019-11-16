#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#gerenciadorMemoriaTest.py

from gerenciadorMemoria import GerenciadorMemoria
from memoriaSecundaria import MemoriaSecundaria

class GerenciadorMemoriaTest:

    def buscarProcessoASerRemovidoTest( self ):
        # Configuração
        caminhoDisco = "discorepositorio.csv"
        processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
        gerenciadorMemoria = GerenciadorMemoria()
        gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( processo )
        gerenciadorMemoria.exibirMapaBits()
