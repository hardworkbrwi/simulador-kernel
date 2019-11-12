#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#kernel.py

import os

from gerenciadorMemoria import GerenciadorMemoria
from memoriaSecundaria import MemoriaSecundaria
from memoriaPrimaria import MemoriaPrimaria
from substituicaoProcesso import SubstituicaoProcesso

def menu():
    print(  "-------- Gerenciador de Memória --------".center(52) )
    print(  "O que você deseja fazer?\n" +
		    "Entre com um dos valores numéricos referêntes aos itens abaixo." )
    print(  "1 - Criar Processo;\n" +
            "2 - Adicionar Processo à memória;\n" +
            "3 - Exibir mapa de bits;\n" +
            "4 - Alterar modo de substituição de processo;\n" +
            "5 - Encerrar processo principal.\n")
    print(  "Obs.: Por default a configuração de substituição de processo é por swapping.\n"+
            "A fim de alterar o modo de substituição para paginação, selecionar a opção 3.\n" )

    menuSelecionado = int( input("Digite um valor: ") )

    print("Você selecionou a opção " + str( menuSelecionado ) + ".\n")

    return menuSelecionado
    
    
if __name__ == '__main__':

    memoriaPrimaria = MemoriaPrimaria()
    TAMANHOPAGINA = 200

    metodoSubstituicaoProcesso = SubstituicaoProcesso.SWAPPING

    if( metodoSubstituicaoProcesso == SubstituicaoProcesso.SWAPPING ):
        gerenciadorMemoria = GerenciadorMemoria()

    else:
        gerenciadorMemoria = GerenciadorMemoria( TAMANHOPAGINA )
    
    while( True ):

        print( "O método de substituição atual é {}\n".format( metodoSubstituicaoProcesso.name ) )
        opcao = menu()

        if( opcao == 1 ):
            # DEFINIR A CRIAÇÃO DE UM PROCESSO E ADICIONÁ-LO NO DISCO
            pass

        elif( opcao == 2 ):
            processo = MemoriaSecundaria.buscarProcesso()
            gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo )

        elif( opcao == 3 ):
            gerenciadorMemoria.exibirMapaBits()

        elif( opcao == 4 ):
            if( metodoSubstituicaoProcesso == SubstituicaoProcesso.SWAPPING ):
                metodoSubstituicaoProcesso = SubstituicaoProcesso.PAGINACAO
                gerenciadorMemoria.tamanhoPagina = TAMANHOPAGINA
                
            else:
                metodoSubstituicaoProcesso = SubstituicaoProcesso.SWAPPING
                gerenciadorMemoria.tamanhoPagina = None

        elif( opcao == 5 ):
            pid = os.getpid()
            os.kill( pid, 15 )

        else:
            print( "A opcão {} é inválida. Favor selecionar uma das opções disponíveis na lista.\n".format( opcao ) )

        