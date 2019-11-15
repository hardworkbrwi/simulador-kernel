#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#processoTest.py

from random import randint

from processo import Processo

class ProcessoTest:

    @staticmethod
    def executarTest():
        # Configuração

        for id in range(10):
            processo = Processo()
            processo.idProcesso = id

            processoEsperado = id

            processo.tamanhoProcesso = randint( 1,50 )
            processo.tempoExecucao = randint( 1,50 )
            processo.tempoVida = randint( 1,50 )
            processo.prioridade = randint( 0, 4 )
            processo.bitR = randint( 0, 1 )
            processo.bitM = randint( 0, 1 )

            # Execução
            processo.executar()

            if( processoEsperado == processo.idProcesso ):
                print( "Esperado: {} == Retornado: {}".format( processo.idProcesso, processoEsperado ) )
            else:
                print( "Esperado: {} != Retornado: {}".format( processo.idProcesso, processoEsperado ) )

    @staticmethod
    def nomeProcessoTest():
        # Configuração

        for id in range(10):
            processo = Processo()
            processo.idProcesso = id
            processo.tamanhoProcesso = randint( 1,50 )
            processo.tempoExecucao = randint( 1,50 )
            processo.tempoVida = randint( 1,50 )
            processo.prioridade = randint( 0, 4 )
            processo.bitR = randint( 0, 1 )
            processo.bitM = randint( 0, 1 )

            # Execução
            nomeProcessoEsperado = str( processo.idProcesso ) + str( processo.tamanhoProcesso ) + str( processo.prioridade ) + str( processo.tempoVida )
            
            if( nomeProcessoEsperado == processo.nomeProcesso ):
                print( "{} == {}".format( processo.nomeProcesso, nomeProcessoEsperado ) )
            else:
                print( "{} != {}".format( processo.nomeProcesso, nomeProcessoEsperado ) )

    @staticmethod
    def exibirProcessoTest():
        # Configuração

        for id in range(10):
            processo = Processo()
            processo.idProcesso = id
            processo.tamanhoProcesso = randint( 1,50 )
            processo.tempoExecucao = randint( 1,50 )
            processo.tempoVida = randint( 1,50 )
            processo.prioridade = randint( 0, 4 )
            processo.bitR = randint( 0, 1 )
            processo.bitM = randint( 0, 1 )

            # Execução
            processo.exibirInfoProcesso()


