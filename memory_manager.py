#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#memory_manager.py

import os

from gerenciadorMemoria import GerenciadorMemoria
from memoriaSecundaria import MemoriaSecundaria
from memoriaPrimaria import MemoriaPrimaria
from substituicaoProcesso import SubstituicaoProcesso

def menu():
    print(  "-------- Gerenciador de Memória --------".center(52) )
    print(  "O que você deseja fazer?\n" +
		    "Entre com um dos valores numéricos referêntes aos itens abaixo." )
    print(  "1 - Adicionar Processo à memória;\n" +
            "2 - Exibir mapa de bits;\n" +
            "3 - Alterar modo de substituição de processo;\n" +
            "4 - Encerrar processo principal.\n")
    print(  "Obs.: Por default a configuração de substituição de processo é por swapping.\n"+
            "A fim de alterar o modo de substituição para paginação, selecionar a opção 3.\n" )

    menuSelecionado = int( input("Digite um valor: ") )

    print("Você selecionou a opção " + str( menuSelecionado ) + ".\n")

    return menuSelecionado
    
    
if __name__ == '__main__':

    memoriaPrimaria = MemoriaPrimaria()

    gerenciadorMemoria = GerenciadorMemoria()

    metodoSubstituicaoProcesso = SubstituicaoProcesso.SWAPPING
    
    while( True ):

        print( "O método de substituição atual é {}\n".format( metodoSubstituicaoProcesso.name ) )
        opcao = menu()

        if( opcao == 1 ):
            if( metodoSubstituicaoProcesso == SubstituicaoProcesso.SWAPPING ):
                processo = MemoriaSecundaria.buscarProcesso()
                gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo )
                
            else:
                # Definir modelo de paginação
                pass

        elif( opcao == 2 ):
            gerenciadorMemoria.exibirMapaBits()

        elif( opcao == 3 ):
            if( metodoSubstituicaoProcesso == SubstituicaoProcesso.SWAPPING ):
                metodoSubstituicaoProcesso = SubstituicaoProcesso.PAGINACAO
            else:
                metodoSubstituicaoProcesso = SubstituicaoProcesso.SWAPPING

        elif( opcao == 4 ):
            pid = os.getpid()
            os.kill( pid, 15 )

        else:
            print( "A opcão {} é inválida. Favor selecionar uma das opções disponíveis na lista.\n".format( opcao ) )

        