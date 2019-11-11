#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#homolog.py

from processo import Processo
from mapeamentoEncadeadoBits import MapeamentoEncadeadoBits
from segmento import Segmento
from memoriaPrimaria import MemoriaPrimaria
from memoriaSecundaria import MemoriaSecundaria
from gerenciadorMemoria import GerenciadorMemoria

def manipularArquivoDiscoTeste():    
    # Configuração

    processo = MemoriaSecundaria.buscarProcesso()
    processo.exibirInfoProcesso()
    
    segmento = Segmento()
    segmento.processo = processo
    segmento.posicaoInicial = 0
    segmento.quantidadePosicoes = processo.tamanhoProcesso

    mapaBits = MapeamentoEncadeadoBits()
    mapaBits.adicionarSegmento( segmento )

    processo1 = MemoriaSecundaria.buscarProcesso()
    processo1.exibirInfoProcesso()
    
    segmento1 = Segmento()
    segmento1.processo = processo1
    segmento1.posicaoInicial = mapaBits.indiceMemoriaLivre
    segmento1.quantidadePosicoes = processo1.tamanhoProcesso

    mapaBits.adicionarSegmento( segmento1 )

    print(mapaBits.indiceMemoriaLivre)

    mapaBits.exibirMapaBits()

    MemoriaSecundaria.armazenarProcesso( processo )
    MemoriaSecundaria.armazenarProcesso( processo1 )

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
    memoriaPrimaria.executarProcessoMemoria( processo, 0 )

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
    memoriaPrimaria.executarProcessoMemoria( processo, posicaoInicialPrimeiroProcesso )

    posicaoInicialSegundoProcesso = processo.tamanhoProcesso
    memoriaPrimaria.executarProcessoMemoria( processo1, posicaoInicialSegundoProcesso )

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
    memoriaPrimaria.executarProcessoMemoria( processo, posicaoInicialPrimeiroProcesso )

    posicaoInicialSegundoProcesso = processo.tamanhoProcesso
    memoriaPrimaria.executarProcessoMemoria( processo1, posicaoInicialSegundoProcesso )

    posicaoInicialTerceiroProcesso = processo.tamanhoProcesso + processo1.tamanhoProcesso
    memoriaPrimaria.executarProcessoMemoria( processo2, posicaoInicialTerceiroProcesso )

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
    memoriaPrimaria.executarProcessoMemoria( processo, posicaoInicialPrimeiroProcesso )

    posicaoInicialSegundoProcesso = processo.tamanhoProcesso
    memoriaPrimaria.executarProcessoMemoria( processo1, posicaoInicialSegundoProcesso )

    posicaoInicialTerceiroProcesso = processo.tamanhoProcesso + processo1.tamanhoProcesso
    memoriaPrimaria.executarProcessoMemoria( processo2, posicaoInicialTerceiroProcesso )

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
    memoriaPrimaria.executarProcessoMemoria( processo, posicaoInicialPrimeiroProcesso )

    posicaoInicialSegundoProcesso = processo.tamanhoProcesso
    memoriaPrimaria.executarProcessoMemoria( processo1, posicaoInicialSegundoProcesso )

    posicaoInicialTerceiroProcesso = processo.tamanhoProcesso + processo1.tamanhoProcesso
    memoriaPrimaria.executarProcessoMemoria( processo2, posicaoInicialTerceiroProcesso )


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

def removeProcessoMemoriaPrimariaQuandoArquivoVazio():
    # Configuração
    processo = Processo()
    processo.idProcesso = 4
    processo.tamanhoProcesso = 200
    processo.tempoExecucao = 2
    processo.tempoVida = 4

    processo1 = MemoriaSecundaria.buscarProcesso()

    gerenciadorMemoria = GerenciadorMemoria()
    
    memoriaPrimaria = MemoriaPrimaria()

    # Execução
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo )
    gerenciadorMemoria.adicionarProcessoMemoriaPrimaria( memoriaPrimaria, processo1 )

    # Validação
    gerenciadorMemoria.exibirMapaBits()






    
if __name__ == '__main__':
    #manipularArquivoDiscoTeste()
    #adicionarUmProcessoMemoriaPrimariaTeste()
    #adicionarDoisProcessoMemoriaPrimariaTeste()
    #adicionarTresProcessoMemoriaPrimariaTeste()
    #adicionarProcessosAcimaCapacidadeMemoriaPrimariaTeste()

    #removerProcessoMemoriaPrimariaTeste()

    #adicionarProcessoGerenciadorMemoriaTeste()

    #adicionarProcessosMaiorGerenciadorMemoria_PrimeiroProcessoNaoRetornaAoDiscoTeste()

    #removeProcessoMemoriaPrimariaQuandoArquivoVazio()