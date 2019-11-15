#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#processo.py
'''
pathfile = './utils/'
if pathfile not in sys.path:
    sys.path.append(pathfile)

from banner import Banner
'''

class Processo:
    '''
    Define um objeto do tipo Processo
    
    :int idProcesso:
    :field idProcesso: identificador único do processo

    :String nomeProcesso:
    :field nomeProcesso: define o nome do processo padronizado por idProcesso+tamanhoProcesso+priorida+tempoVida

    :int tamanhoProcesso:
    :field tamanhoProcesso: define o tamanho do processo em kilobytes

    :int tempoExecucao:
    :field tempoExecucao: define o tempo ao qual o processo deverá executar em CPU

    :int prioridade:
    :field prioridade: define a prioridade de escalonamento para execução no processador

    :int tempoVida:
    :field tempoVida: define o tempo de vida útil do processo

    :byte bitR:
    :field bitR: indentifica se a página do processo foi referenciada ou não

    :byte bitM:
    :field bitM: identificador se a página do processo foi modificada ou não
    '''

    __slots__ = [ "_idProcesso", "_nomeProcesso", "_tamanhoProcesso", "_tempoExecucao", "_prioridade", "_tempoVida", "_bitR", "_bitM" ]

    def __init__( self, tempoExecucao = 2, prioridade = 4 ):
        self._idProcesso = 0
        self._nomeProcesso = ""
        self._tamanhoProcesso = 0
        self._tempoExecucao = tempoExecucao
        self._prioridade = prioridade
        self._tempoVida = 0
        self._bitR = 0
        self._bitM = 0

    def executar( self ):
        '''
        Inicializa a execuação do processo após sua alocação na memória principal
        '''
        print( "Processo {} está executando.".format( self._idProcesso ) )

    def exibirInfoProcesso( self ):
        print( "ID: {}\nNome Processo: {}\nTamanho: {}\nTempo Execução: {}\nPrioridade: {}\nTempo Vida: {}\nBitR: {}\nBitM: {}".format( self._idProcesso, self._nomeProcesso, self._tamanhoProcesso, self._tempoExecucao, self._prioridade ,self._tempoVida, self._bitR, self._bitM ) )

    @property
    def idProcesso( self ):
        return self._idProcesso
    
    @idProcesso.setter
    def idProcesso( self, idProcesso ):
        self._idProcesso = int( idProcesso )
        self._definirNomeProcesso()

    @property
    def nomeProcesso( self ):
        return self._nomeProcesso
    
    def _definirNomeProcesso( self ):
        self._nomeProcesso = str( self._idProcesso ) + str( self._tamanhoProcesso ) + str( self._prioridade ) + str( self._tempoVida )

    @property
    def tamanhoProcesso( self ):
        return self._tamanhoProcesso
    
    @tamanhoProcesso.setter
    def tamanhoProcesso( self, tamanhoProcesso ):
        self._tamanhoProcesso = int( tamanhoProcesso )
        self._definirNomeProcesso()

    @property
    def tempoExecucao( self ):
        return self._tempoExecucao
    
    @tempoExecucao.setter
    def tempoExecucao( self, tempoExecucao ):
        self._tempoExecucao = int( tempoExecucao )

    @property
    def prioridade( self ):
        return self._prioridade
    
    @prioridade.setter
    def prioridade( self, prioridade ):
        self._prioridade = int( prioridade )
        self._definirNomeProcesso()
    
    @property
    def tempoVida( self ):
        return self._tempoVida
    
    @tempoVida.setter
    def tempoVida( self, tempoVida ):
        self._tempoVida = int( tempoVida )
        self._definirNomeProcesso()

    @property
    def bitR( self ):
        return self._bitR
    
    @bitR.setter
    def bitR( self, bitR ):
        self._bitR = int( bitR )

    @property
    def bitM( self ):
        return self._bitM
    
    @bitM.setter
    def bitM( self, bitM ):
        self._bitM = int( bitM )
    

    

