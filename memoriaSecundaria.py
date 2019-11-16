#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#memoriaSecundaria.py

from processo import Processo

class MemoriaSecundaria:
    """
    Define um objeto abstraindo a memória secundária do computador
    """

    @staticmethod
    def buscarProcessoDisco( caminhoDisco ):
        '''
        Busca o primeiro processo na fila de processo contida no arquivo (caminhoDisco) 
        '''
        try:
            arquivo = open( caminhoDisco, 'r' )

        except IOError as io:
            print( "Não foi possível abrir o arquivo {}".format( io ) )

        else:
            processosStr = arquivo.readlines()
            arquivo.close()
            
            processo = None

            tamanhoListaProcesso = len( processosStr )
            if( tamanhoListaProcesso != 0 ):
                indicePrioridadeMaisAlta = MemoriaSecundaria._buscarProcessoNivelAltoPrioridadeDisco( processosStr )
                processoStr = processosStr.pop( indicePrioridadeMaisAlta )

                MemoriaSecundaria._gravarDisco( processosStr, caminhoDisco )

                try:
                    processo = MemoriaSecundaria._converterStringParaProcesso( processoStr )

                except ValueError as vl:
                    print( "O processo está quebrado. Quantidade de argumentos é inválida.\n{}".format(vl) )
                
        return processo

    @staticmethod
    def armazenarProcessoDisco( processo, caminhoDisco ):
        '''
        Realoca o processo com execução incompleta no caminhoDisco
        '''
        try:
            arquivo = open( caminhoDisco, 'r' )

        except IOError as io:
            print( "Não foi possível abrir o arquivo {}".format( io ) )

        else:
            processosStr = arquivo.readlines()
            processoRealocado = MemoriaSecundaria._converterProcessoParaString( processo )
            processosStr.append( processoRealocado )            

            MemoriaSecundaria._gravarDisco( processosStr, caminhoDisco )
        
        finally:
            arquivo.close()

    @classmethod
    def _buscarProcessoNivelAltoPrioridadeDisco( cls, processosStr ):
        indiceAtualPrioridade = 0
        nivelAtualPrioridade = 4
        for indice, processoStr in enumerate( processosStr ):
            processo = cls._converterStringParaProcesso( processoStr )
            if( processo.prioridade < nivelAtualPrioridade ):
                indiceAtualPrioridade = indice
                nivelAtualPrioridade = processo.prioridade

        return indiceAtualPrioridade

    @classmethod
    def _gravarDisco( cls, processosStr, caminhoDisco ):
        try:
            arquivo = open( caminhoDisco, 'w' )

        except IOError as io:
            print( "Não foi possível abrir o arquivo {}".format( io ) )

        else:
            for processoStr in processosStr:
                arquivo.writelines( processoStr )

        finally:
            arquivo.close()

    @classmethod
    def _converterStringParaProcesso( cls, processoStr ):
        """
        Faz o tratamento das informações do processo contidas na String

        :String processoStr:
        :param processoStr: metadados do Processo contidas na String

        :return: Retorna o objeto Processo com os seus devidos metadados
        """
        tamanhoListaProcesso = len( processoStr )
        if( tamanhoListaProcesso != 0 ):
            infoProcessoTemp = processoStr.replace( ' ', '' )
            infoProcesso = infoProcessoTemp.split( ',' ) 

            try:
                quantidadeItensInfoProcesso = len( infoProcesso )
                if( quantidadeItensInfoProcesso != 6 ):
                    raise ValueError

                else:
                    processo = Processo()
                    processo.idProcesso = infoProcesso[0]
                    #processo.nomeProcesso = infoProcesso[1]
                    processo.tamanhoProcesso = infoProcesso[2]
                    processo.tempoExecucao = infoProcesso[3]
                    processo.prioridade = infoProcesso[4]
                    processo.tempoVida = infoProcesso[5]

                    return processo

            except ValueError:
                raise ValueError

        else:
            return processo

    @classmethod
    def _converterProcessoParaString( cls, processo ):
        """
        Faz o tratamento das informações do processo contidas na String

        :String processoStr:
        :param processoStr: metadados do Processo contidas na String

        :return: Retorna o objeto Processo com os seus devidos metadados
        """
        VIRGULA = ","
        QUEBRA_LINHA = "\n"
        
        processoStr = []
        processoStr.append( str(processo.idProcesso) + VIRGULA )
        processoStr.append( str(processo.nomeProcesso) + VIRGULA )
        processoStr.append( str(processo.tamanhoProcesso) + VIRGULA )
        processoStr.append( str(processo.tempoExecucao) + VIRGULA )
        processoStr.append( str(processo.prioridade) + VIRGULA )
        processoStr.append( str(processo.tempoVida) + QUEBRA_LINHA)

        return processoStr


        