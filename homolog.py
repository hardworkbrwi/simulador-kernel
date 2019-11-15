#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#homolog.py

from random import randint

from processo import Processo
from mapeamentoEncadeadoBits import MapeamentoEncadeadoBits
from segmento import Segmento
from memoriaPrimaria import MemoriaPrimaria
from memoriaSecundaria import MemoriaSecundaria
from gerenciadorMemoria import GerenciadorMemoria
from processador import Processador
from kernel import criarProcesso


def manipularArquivoDiscoTeste():    
    # Configuração
    caminhoDisco = "disco.csv"

    processo = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
    processo.exibirInfoProcesso()
    
    segmento = Segmento()
    segmento.processo = processo
    segmento.posicaoInicial = 0
    segmento.quantidadePosicoes = processo.tamanhoProcesso

    mapaBits = MapeamentoEncadeadoBits()
    mapaBits.adicionarSegmento( segmento )

    processo1 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )
    processo1.exibirInfoProcesso()
    
    segmento1 = Segmento()
    segmento1.processo = processo1
    segmento1.posicaoInicial = mapaBits.indiceMemoriaLivre
    segmento1.quantidadePosicoes = processo1.tamanhoProcesso

    mapaBits.adicionarSegmento( segmento1 )

    print(mapaBits.indiceMemoriaLivre)

    mapaBits.exibirMapaBits()

    MemoriaSecundaria.armazenarProcesso( processo, caminhoDisco )
    MemoriaSecundaria.armazenarProcesso( processo1, caminhoDisco )

    mapaBits.removerSegmento()

    print(mapaBits.indiceMemoriaLivre)

    mapaBits.exibirMapaBits()

def adicionarUmProcessoMemoriaPrimariaTeste():
    # Configuração
    processo = Processo()
    processo.idProcesso = 1
    processo.tamanhoProcesso = 350
    processo.tempoVida = 10

    # Execução
    memoriaPrimaria = MemoriaPrimaria()
    memoriaPrimaria.adicionarProcessoMemoria( processo, 0 )

    # Verificação
    memoriaPrimaria.exibirMemoriaPrimaria()

def adicionarDoisProcessoMemoriaPrimariaTeste():
    # Configuração
    processo = Processo()
    processo.idProcesso = 1
    processo.tamanhoProcesso = 12
    processo.tempoVida = 10

    processo1 = Processo()
    processo1.idProcesso = 2
    processo1.tamanhoProcesso = 14
    processo1.tempoVida = 10

    # Execução
    memoriaPrimaria = MemoriaPrimaria()

    posicaoInicialPrimeiroProcesso = 0
    memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicialPrimeiroProcesso )

    posicaoInicialSegundoProcesso = processo.tamanhoProcesso
    memoriaPrimaria.adicionarProcessoMemoria( processo1, posicaoInicialSegundoProcesso )

    # Verificação
    memoriaPrimaria.exibirMemoriaPrimaria()

def adicionarTresProcessoMemoriaPrimariaTeste():
    # Configuração
    processo = Processo()
    processo.idProcesso = 1
    processo.tamanhoProcesso = 12
    processo.tempoVida = 10

    processo1 = Processo()
    processo1.idProcesso = 2
    processo1.tamanhoProcesso = 14
    processo1.tempoVida = 10

    processo2 = Processo()
    processo2.idProcesso = 3
    processo2.tamanhoProcesso = 10
    processo2.tempoVida = 10

    # Execução
    memoriaPrimaria = MemoriaPrimaria()
    
    posicaoInicialPrimeiroProcesso = 0
    memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicialPrimeiroProcesso )

    posicaoInicialSegundoProcesso = processo.tamanhoProcesso
    memoriaPrimaria.adicionarProcessoMemoria( processo1, posicaoInicialSegundoProcesso )

    posicaoInicialTerceiroProcesso = processo.tamanhoProcesso + processo1.tamanhoProcesso
    memoriaPrimaria.adicionarProcessoMemoria( processo2, posicaoInicialTerceiroProcesso )

    # Verificação
    memoriaPrimaria.exibirMemoriaPrimaria()

def adicionarProcessosAcimaCapacidadeMemoriaPrimariaTeste():
    # VERIFICAR PROBLEMA DE QUANTIDADE MÁXIMA DE ELEMENTOS NA LISTA 
    # Unable to handle: unable to handle: too large to show contents
    # Configuração
    processo = Processo()
    processo.idProcesso = 1
    processo.tamanhoProcesso = 1020
    processo.tempoVida = 10

    processo1 = Processo()
    processo1.idProcesso = 2
    processo1.tamanhoProcesso = 1020
    processo1.tempoVida = 10

    processo2 = Processo()
    processo2.idProcesso = 3
    processo2.tamanhoProcesso = 10
    processo2.tempoVida = 10

    # Execução
    memoriaPrimaria = MemoriaPrimaria()
    
    posicaoInicialPrimeiroProcesso = 0
    memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicialPrimeiroProcesso )

    posicaoInicialSegundoProcesso = processo.tamanhoProcesso
    memoriaPrimaria.adicionarProcessoMemoria( processo1, posicaoInicialSegundoProcesso )

    posicaoInicialTerceiroProcesso = processo.tamanhoProcesso + processo1.tamanhoProcesso
    memoriaPrimaria.adicionarProcessoMemoria( processo2, posicaoInicialTerceiroProcesso )

    # Verificação
    memoriaPrimaria.exibirMemoriaPrimaria()

def removerProcessoMemoriaPrimariaTeste():
    # Configuração
    processo = Processo()
    processo.idProcesso = 1
    processo.tamanhoProcesso = 12
    processo.tempoVida = 10

    processo1 = Processo()
    processo1.idProcesso = 2
    processo1.tamanhoProcesso = 14
    processo1.tempoVida = 10

    processo2 = Processo()
    processo2.idProcesso = 3
    processo2.tamanhoProcesso = 10
    processo2.tempoVida = 10

    # Execução
    memoriaPrimaria = MemoriaPrimaria()
    
    posicaoInicialPrimeiroProcesso = 0
    memoriaPrimaria.adicionarProcessoMemoria( processo, posicaoInicialPrimeiroProcesso )

    posicaoInicialSegundoProcesso = processo.tamanhoProcesso
    memoriaPrimaria.adicionarProcessoMemoria( processo1, posicaoInicialSegundoProcesso )

    posicaoInicialTerceiroProcesso = processo.tamanhoProcesso + processo1.tamanhoProcesso
    memoriaPrimaria.adicionarProcessoMemoria( processo2, posicaoInicialTerceiroProcesso )


    # Verificação
    memoriaPrimaria.exibirMemoriaPrimaria()
    
    memoriaPrimaria.liberarMemoria()
    memoriaPrimaria.exibirMemoriaPrimaria()

    memoriaPrimaria.liberarMemoria()
    memoriaPrimaria.exibirMemoriaPrimaria()

def adicionarProcessoGerenciadorMemoriaTeste():
    processo = Processo()
    processo.idProcesso = 45
    processo.tamanhoProcesso = 12
    processo.tempoExecucao = 2
    processo.tempoVida = 8

    memoriaPrimaria = MemoriaPrimaria()

    gerenciadorMemoria = GerenciadorMemoria()
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo )

    memoriaPrimaria.exibirMemoriaPrimaria()

    gerenciadorMemoria.exibirMapaBits()

def adicionarProcessosMaiorMemoriaGerenciadorMemoriaTeste():
    # Configuração
    processo = Processo()
    processo.idProcesso = 1
    processo.tamanhoProcesso = 1020
    processo.tempoVida = 10

    processo1 = Processo()
    processo1.idProcesso = 2
    processo1.tamanhoProcesso = 1020
    processo1.tempoVida = 10

    processo2 = Processo()
    processo2.idProcesso = 3
    processo2.tamanhoProcesso = 10
    processo2.tempoVida = 10

    memoriaPrimaria = MemoriaPrimaria()

    gerenciadorMemoria = GerenciadorMemoria()

    # Execução
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( processo, memoriaPrimaria )
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( processo1, memoriaPrimaria )
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( processo2, memoriaPrimaria )

    #Validação
    memoriaPrimaria.exibirMemoriaPrimaria()

    gerenciadorMemoria.exibirMapaBits()

def adicionarProcessosMaiorGerenciadorMemoria_PrimeiroProcessoNaoRetornaAoDiscoTeste():
    # Configuração
    processo = Processo()
    processo.idProcesso = 1
    processo.tamanhoProcesso = 1020
    processo.tempoVida = 2

    processo1 = Processo()
    processo1.idProcesso = 2
    processo1.tamanhoProcesso = 1020
    processo1.tempoVida = 10

    processo2 = Processo()
    processo2.idProcesso = 3
    processo2.tamanhoProcesso = 10
    processo2.tempoVida = 10

    memoriaPrimaria = MemoriaPrimaria()

    gerenciadorMemoria = GerenciadorMemoria()

    # Execução
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo )
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo1 )
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo2 )

    #Validação
    memoriaPrimaria.exibirMemoriaPrimaria()

    gerenciadorMemoria.exibirMapaBits()

def removeProcessoMemoriaPrimariaQuandoArquivoVazioTeste():
    # Configuração
    processo = Processo()
    processo.idProcesso = 4
    processo.tamanhoProcesso = 200
    processo.tempoExecucao = 2
    processo.tempoVida = 4

    caminhoDisco = "disco.csv"
    processo1 = MemoriaSecundaria.buscarProcessoDisco( caminhoDisco )

    gerenciadorMemoria = GerenciadorMemoria()
    
    memoriaPrimaria = MemoriaPrimaria()

    # Execução
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo )
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo1 )

    # Validação
    gerenciadorMemoria.exibirMapaBits()

def executarProcesso():
    processo = Processo()
    processo.idProcesso = 4
    processo.tamanhoProcesso = 200
    processo.tempoExecucao = 2
    processo.tempoVida = 1

    processador = Processador()

    print(processador.executar(processo))
    
def escalonarProcessos():
    
    memoriaPrimaria = MemoriaPrimaria()
    gerenciadorMemoria = GerenciadorMemoria()
    processador = Processador()

    for id in range(10):
        processo = Processo()
        processo.idProcesso = id
        processo.tamanhoProcesso = randint( 1,50 )
        processo.tempoExecucao = randint( 1,50 )
        processo.tempoVida = randint( 1,50 )
        processo.prioridade = randint( 0, 4 )
        gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo )

    processador.montarTabelaDeExecucaoDeProcessos( memoriaPrimaria )
    
    if processador.escalonadorDeProcesso() != None:
        print(processador.escalonadorDeProcesso().exibirInfoProcesso())

    #Validação
    memoriaPrimaria.exibirMemoriaPrimaria()

    gerenciadorMemoria.exibirMapaBits()

def gerarAdicionarNovoProcessoDiscoTeste():
    # Configuração
    idProcesso = randint( 5000, 6000 )
    processosStr = []
    processoStr = ""
    processoEsperado = Processo()

    caminhoDisco = "discorepositorio.csv"    

    # Execução
    processoAArmazenar = criarProcesso( idProcesso )
    MemoriaSecundaria.armazenarProcesso( processoAArmazenar, caminhoDisco )

    try:
        disco = open( caminhoDisco, "r" )

    except IOError as io:
        print( "Não foi possível abrir o arquivo {}".format( io ) )

    else:
        processosStr = disco.readlines()
        disco.close()
    
    processoStr = processosStr[-1]

    # Validação
    processoEsperado = MemoriaSecundaria._converterStringParaProcesso( processoStr )
    processoEsperado.exibirInfoProcesso()
    
if __name__ == '__main__':
    #manipularArquivoDiscoTeste()
    #adicionarUmProcessoMemoriaPrimariaTeste()
    #adicionarDoisProcessoMemoriaPrimariaTeste()
    #adicionarTresProcessoMemoriaPrimariaTeste()
    #adicionarProcessosAcimaCapacidadeMemoriaPrimariaTeste()

    #removerProcessoMemoriaPrimariaTeste()

    #adicionarProcessoGerenciadorMemoriaTeste()

    #adicionarProcessosMaiorGerenciadorMemoria_PrimeiroProcessoNaoRetornaAoDiscoTeste()

    #removeProcessoMemoriaPrimariaQuandoArquivoVazioTeste()

    #executarProcesso()
    #escalonarProcessos()

    gerarAdicionarNovoProcessoDiscoTeste()