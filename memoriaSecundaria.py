#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#memoriaSecundaria.py

from processo import Processo

class MemoriaSecundaria:
    """
    Define um objeto abstraindo a memória secundária do computador
    """

    @staticmethod
    def buscarProcesso():
        '''
        Busca o primeiro processo na fila de processo contida no arquivo (disco) 
        '''
        try:
            arquivo = open( 'disco.csv', 'r' )

        except IOError as io:
            print( "Não foi possível abrir o arquivo {}".format( io ) )

        else:
            processosStr = arquivo.readlines()
            arquivo.close()
            
            processo = None

            tamanhoListaProcesso = len( processosStr )
            if( tamanhoListaProcesso != 0 ):
                processoStr = processosStr.pop(0)

                MemoriaSecundaria._gravarDisco( processosStr )

                try:
                    processo = MemoriaSecundaria._converterStringParaProcesso( processoStr )

                except ValueError as vl:
                    print( "O processo está quebrado. Quantidade de argumentos é inválida.\n{}".format(vl) )
                
        return processo

    @staticmethod
    def armazenarProcesso( processo ):
        '''
        Realoca o processo com execução incompleta no disco
        '''
        try:
            arquivo = open( 'disco.csv', 'r' )
            #arquivo = open( 'discorepositorio.csv', 'r' )
            

        except IOError as io:
            print( "Não foi possível abrir o arquivo {}".format( io ) )

        else:
            processosStr = arquivo.readlines()
            processoRealocado = MemoriaSecundaria._converterProcessoParaString( processo )
            processosStr.append( processoRealocado )            

            MemoriaSecundaria._gravarDisco( processosStr )
        
        finally:
            arquivo.close()

    @classmethod
    def _gravarDisco( cls, processosStr ):
        try:
            arquivo = open( 'disco.csv', 'w' )
            #arquivo = open( 'discorepositorio.csv', "w" )

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
                if( quantidadeItensInfoProcesso != 4 ):
                    raise ValueError

                else:
                    processo = Processo()
                    processo.idProcesso = infoProcesso[0]
                    processo.tamanhoProcesso = infoProcesso[1]
                    processo.tempoExecucao = infoProcesso[2]
                    processo.tempoVida = infoProcesso[3]

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
        processoStr.append( str(processo.tamanhoProcesso) + VIRGULA )
        processoStr.append( str(processo.tempoExecucao) + VIRGULA )
        processoStr.append( str(processo.tempoVida) + QUEBRA_LINHA)

        return processoStr


        