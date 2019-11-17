#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#kernel.py

import os
from random import randint

from processo import Processo
from processador import Processador
from gerenciadorMemoria import GerenciadorMemoria
from memoriaSecundaria import MemoriaSecundaria
from memoriaPrimaria import MemoriaPrimaria
from substituicaoProcesso import SubstituicaoProcesso


def menu():
    print(  "-------- Simulador de Kernel de S.O. --------".center(52) )
    print(  "O que você deseja fazer?\n" +
		    "Entre com um dos valores numéricos referêntes aos itens abaixo." )
    print(  "1 - Criar Processo;\n" +
            "2 - Executar Processo;\n" +
            "3 - Exibir mapa de bits;\n" +
            "4 - Encerrar processo principal.\n")

    menuSelecionado = int( input("Digite um valor: ") )

    print("Você selecionou a opção " + str( menuSelecionado ) + ".\n")

    return menuSelecionado

def criarProcesso( idProcesso ):
    processo = Processo()
    processo.idProcesso = idProcesso
    processo.tamanhoProcesso = randint( 100, 1024 )
    #processo.tempoExecucao = 2
    processo.prioridade = randint( 0, 4 )
    processo.tempoVida = randint( 1, 15 )
    #processo.nomeProcesso = str( idProcesso ) + str( processo.tamanhoProcesso ) + str( processo.prioridade ) + str( processo.tempoVida )
    
    return processo
    
if __name__ == '__main__':

    opcao = -1
    while opcao < 1 or opcao > 2 :
        print( "Que modo de substituição de processo deseja usar?" )
        print( '''1 - {};\n2 - {}.'''.format( "SWAPPING", "PAGINAÇÃO" ) )
        opcao = int( input( "Digite o valor: " ) )
        
        if( opcao < 1 or opcao > 2 ):
            print( "O valor {} que você entrou é inválido.\nFavor Selecionar uma dos valores acima.".format(opcao) )

    TAMANHOPAGINA = 200
    gerenciadorMemoria = GerenciadorMemoria()
    if( opcao == 1 ):
        metodoSubstituicaoProcesso = SubstituicaoProcesso.SWAPPING
        gerenciadorMemoria.tamanhoPagina = None

    else:
        metodoSubstituicaoProcesso = SubstituicaoProcesso.PAGINACAO
        gerenciadorMemoria.tamanhoPagina = TAMANHOPAGINA   

    contadorIdProcesso = 1000

    # Caminho para o disco físico (arquivo)
    caminhoDisco = "disco.csv"

    memoriaPrimaria = MemoriaPrimaria()
    processador = Processador()
    while( True ):

        print( "O método de substituição atual é {}\n".format( metodoSubstituicaoProcesso.name ) )
        opcao = menu()

        if( opcao == 1 ):
            novoProcesso = criarProcesso( contadorIdProcesso )
            MemoriaSecundaria.armazenarProcessoDisco( novoProcesso, caminhoDisco )
            contadorIdProcesso += 1

        elif( opcao == 2 ):

            memoriaVazia = memoriaPrimaria.memoriaEstaVazia()

            novoProcesso = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )

            if( memoriaVazia and novoProcesso == None ): # A) M0 e D0
                print( "O sistema será encerrado por indisponibilidade de processos." )
                pid = os.getpid()
                os.kill( pid, 15 )

            else:
                if( novoProcesso != None ): #D1
                    tamanhoMaxMemoria = memoriaPrimaria.tamanhoMemoria
                    quantidadePosicoesOcupadasMemoria = len( memoriaPrimaria.posicoesMemoria )
                    tamanhoNovoProcesso = novoProcesso.tamanhoProcesso

                    if( quantidadePosicoesOcupadasMemoria + tamanhoNovoProcesso > tamanhoMaxMemoria ):
                        listaProcessosRemovidos = gerenciadorMemoria.liberarEspacoMemoriaPrimaria( memoriaPrimaria, tamanhoNovoProcesso )
                        processador.montarTabelaDeExecucaoDeProcessos( memoriaPrimaria )

                        for processoRemovidoAtual in listaProcessosRemovidos:
                            if( processoRemovidoAtual.tempoVida > 0 ):
                                MemoriaSecundaria.armazenarProcessoDisco( processoRemovidoAtual, caminhoDisco )
                    
                    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, novoProcesso )
                    processador.montarTabelaDeExecucaoDeProcessos( memoriaPrimaria )
                
                processoEscalonado = processador.escalonadorDeProcesso()
                gerenciadorMemoria.atualizarBitRProcessosNaoReferenciados()
                gerenciadorMemoria.atualizaBitsReferenciaModificacaoMemoriaPrimaria( memoriaPrimaria, processoEscalonado )
                flagConclusao = processador.executar( processoEscalonado )

                if( flagConclusao == -1 ):
                    espacoASerRemovido = gerenciadorMemoria.tamanhoPagina
                    gerenciadorMemoria.liberarEspacoMemoriaPrimaria( memoriaPrimaria, espacoASerRemovido, processoEscalonado )
                    processador.montarTabelaDeExecucaoDeProcessos( memoriaPrimaria )

                elif( flagConclusao == 1 ):
                    gerenciadorMemoria.atualizarTempoVidaProcesso( memoriaPrimaria, processoEscalonado )

                elif( flagConclusao == 0 ):
                    gerenciadorMemoria.atualizaBitsReferenciaNaoModificacaoMemoriaPrimaria( memoriaPrimaria, processoEscalonado )

        elif( opcao == 3 ):
            gerenciadorMemoria.exibirMapaBits()

        elif( opcao == 4 ):
            pid = os.getpid()
            os.kill( pid, 15 )

        else:
            print( "A opcão {} é inválida. Favor selecionar uma das opções disponíveis na lista.\n".format( opcao ) )

        