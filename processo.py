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

    :int tamanhoProcesso:
    :field tamanhoProcesso: define o tamanho do processo em kilobytes

    :int tempoExecucao:
    :field tempoExecucao: define o tempo ao qual o processo deverá executar em CPU

    :int tempoVida:
    :field tempoVida: define o tempo de vida útil do processo
    '''

    __slots__ = [ "_idProcesso", "_tamanhoProcesso", "_tempoExecucao", "_tempoVida" ]

    def __init__( self, tempoExecucao = 2 ):
        self._tempoExecucao = tempoExecucao

    def executar( self ):
        '''
        Inicializa a execuação do processo após sua alocação na memória principal
        '''
        print( "Processo {} está executando.".format( self._idProcesso ) )

    def exibirInfoProcesso( self ):
        print( "ID: {}\nTamanho: {}\nTempo Execução: {}\nTempo Vida: {}".format( self._idProcesso,
        self._tamanhoProcesso, self._tempoExecucao, self._tempoVida ) )

    @property
    def idProcesso( self ):
        return self._idProcesso
    
    @idProcesso.setter
    def idProcesso( self, idProcesso ):
        self._idProcesso = int( idProcesso )

    @property
    def tamanhoProcesso( self ):
        return self._tamanhoProcesso
    
    @tamanhoProcesso.setter
    def tamanhoProcesso( self, tamanhoProcesso ):
        self._tamanhoProcesso = int( tamanhoProcesso )

    @property
    def tempoExecucao( self ):
        return self._tempoExecucao
    
    @tempoExecucao.setter
    def tempoExecucao( self, tempoExecucao ):
        self._tempoExecucao = int( tempoExecucao )

    @property
    def tempoVida( self ):
        return self._tempoVida
    
    @tempoVida.setter
    def tempoVida( self, tempoVida ):
        self._tempoVida = int( tempoVida )
    
    @property
    def prioridade( self ):
        return self.prioridade
    
    @prioridade.setter
    def prioridade( self, prioridade ):
        self.prioridade = int( prioridade )
        pass

    

