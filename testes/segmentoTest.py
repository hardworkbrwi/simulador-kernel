#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#segmentoTest.py

from random import randint

from processo import Processo
from segmento import Segmento

class SegmentoTest:
    

    @staticmethod
    def definirClasseSubstituicaoPaginaClasse0Test():
        # Configuração
        print( "definirClasseSubstituicaoPaginaClasse0Test: " )
        processo = Processo()
        segmento = Segmento()
        classeEsperada = -1
        processo.bitR = 0
        processo.bitM = 0

        # Execução
        if( processo.bitR  == 0 and processo.bitM == 0 ):
            classeEsperada = 0

        elif( processo.bitR  == 0 and processo.bitM == 1 ):
            classeEsperada = 1

        elif( processo.bitR  == 1 and processo.bitM == 0 ):
            classeEsperada = 2

        elif( processo.bitR  == 1 and processo.bitM == 1 ):
            classeEsperada = 3

        else:
            classeEsperada = -1

        segmento.processo = processo

        # Validação
        segmento.definirClasseSubstituicaoPagina()
        if( classeEsperada == segmento.classeSubstituicao ):
            print( "Esperado: {} == Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )
        else:
            print( "Esperado: {} != Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )

    @staticmethod
    def definirClasseSubstituicaoPaginaClasse1Test():
        print( "definirClasseSubstituicaoPaginaClasse1Test: " )
        processo = Processo()
        segmento = Segmento()
        classeEsperada = -1
        processo.bitR = 0
        processo.bitM = 1

        # Execução
        if( processo.bitR  == 0 and processo.bitM == 0 ):
            classeEsperada = 0

        elif( processo.bitR  == 0 and processo.bitM == 1 ):
            classeEsperada = 1

        elif( processo.bitR  == 1 and processo.bitM == 0 ):
            classeEsperada = 2

        elif( processo.bitR  == 1 and processo.bitM == 1 ):
            classeEsperada = 3

        else:
            classeEsperada = -1

        segmento.processo = processo

        # Validação
        segmento.definirClasseSubstituicaoPagina()
        if( classeEsperada == segmento.classeSubstituicao ):
            print( "Esperado: {} == Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )
        else:
            print( "Esperado: {} != Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )

    @staticmethod
    def definirClasseSubstituicaoPaginaClasse2Test():
        print( "definirClasseSubstituicaoPaginaClasse2Test: " )
        processo = Processo()
        segmento = Segmento()
        classeEsperada = -1
        processo.bitR = 1
        processo.bitM = 0

        # Execução
        if( processo.bitR  == 0 and processo.bitM == 0 ):
            classeEsperada = 0

        elif( processo.bitR  == 0 and processo.bitM == 1 ):
            classeEsperada = 1

        elif( processo.bitR  == 1 and processo.bitM == 0 ):
            classeEsperada = 2

        elif( processo.bitR  == 1 and processo.bitM == 1 ):
            classeEsperada = 3

        else:
            classeEsperada = -1

        segmento.processo = processo

        # Validação
        segmento.definirClasseSubstituicaoPagina()
        if( classeEsperada == segmento.classeSubstituicao ):
            print( "Esperado: {} == Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )
        else:
            print( "Esperado: {} != Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )

    @staticmethod
    def definirClasseSubstituicaoPaginaClasse3Test():
        print( "definirClasseSubstituicaoPaginaClasse3Test: " )
        processo = Processo()
        segmento = Segmento()
        classeEsperada = -1
        processo.bitR = 1
        processo.bitM = 1

        # Execução
        if( processo.bitR  == 0 and processo.bitM == 0 ):
            classeEsperada = 0

        elif( processo.bitR  == 0 and processo.bitM == 1 ):
            classeEsperada = 1

        elif( processo.bitR  == 1 and processo.bitM == 0 ):
            classeEsperada = 2

        elif( processo.bitR  == 1 and processo.bitM == 1 ):
            classeEsperada = 3

        else:
            classeEsperada = -1

        segmento.processo = processo

        # Validação
        segmento.definirClasseSubstituicaoPagina()
        if( classeEsperada == segmento.classeSubstituicao ):
            print( "Esperado: {} == Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )
        else:
            print( "Esperado: {} != Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )

    @staticmethod
    def definirClasseSubstituicaoPaginaBitRIndefinidoBitM0Test():
        print( "definirClasseSubstituicaoPaginaBitRIndefinidoBitM0Test: " )
        processo = Processo()
        segmento = Segmento()
        classeEsperada = -1
        processo = Processo()
        processo.bitR = -1
        processo.bitM = 0

        segmento = Segmento()

        # Execução
        classeEsperada = -1

        if( processo.bitR  == 0 and processo.bitM == 0 ):
            classeEsperada = 0

        elif( processo.bitR  == 0 and processo.bitM == 1 ):
            classeEsperada = 1

        elif( processo.bitR  == 1 and processo.bitM == 0 ):
            classeEsperada = 2

        elif( processo.bitR  == 1 and processo.bitM == 1 ):
            classeEsperada = 3

        else:
            classeEsperada = -1

        segmento.processo = processo

        # Validação
        segmento.definirClasseSubstituicaoPagina()
        if( classeEsperada == segmento.classeSubstituicao ):
            print( "Esperado: {} == Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )
        else:
            print( "Esperado: {} != Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )

    @staticmethod
    def definirClasseSubstituicaoPaginaBitRIndefinidoBitM1Test():
        print( "definirClasseSubstituicaoPaginaBitRIndefinidoBitM1Test: " )
        processo = Processo()
        segmento = Segmento()
        classeEsperada = -1
        processo = Processo()
        processo.bitR = -1
        processo.bitM = 1

        segmento = Segmento()

        # Execução
        classeEsperada = -1

        if( processo.bitR  == 0 and processo.bitM == 0 ):
            classeEsperada = 0

        elif( processo.bitR  == 0 and processo.bitM == 1 ):
            classeEsperada = 1

        elif( processo.bitR  == 1 and processo.bitM == 0 ):
            classeEsperada = 2

        elif( processo.bitR  == 1 and processo.bitM == 1 ):
            classeEsperada = 3

        else:
            classeEsperada = -1

        segmento.processo = processo

        # Validação
        segmento.definirClasseSubstituicaoPagina()
        if( classeEsperada == segmento.classeSubstituicao ):
            print( "Esperado: {} == Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )
        else:
            print( "Esperado: {} != Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )

    @staticmethod
    def definirClasseSubstituicaoPaginaBitR0BitMIndefinidoTest():
        print( "definirClasseSubstituicaoPaginaBitR0BitMIndefinidoTest: " )
        processo = Processo()
        segmento = Segmento()
        classeEsperada = -1
        processo = Processo()
        processo.bitR = 0
        processo.bitM = -1

        segmento = Segmento()

        # Execução
        classeEsperada = -1

        if( processo.bitR  == 0 and processo.bitM == 0 ):
            classeEsperada = 0

        elif( processo.bitR  == 0 and processo.bitM == 1 ):
            classeEsperada = 1

        elif( processo.bitR  == 1 and processo.bitM == 0 ):
            classeEsperada = 2

        elif( processo.bitR  == 1 and processo.bitM == 1 ):
            classeEsperada = 3

        else:
            classeEsperada = -1

        segmento.processo = processo

        # Validação
        segmento.definirClasseSubstituicaoPagina()
        if( classeEsperada == segmento.classeSubstituicao ):
            print( "Esperado: {} == Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )
        else:
            print( "Esperado: {} != Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )

    @staticmethod
    def definirClasseSubstituicaoPaginaBitR1BitMIndefinidoTest():
        print( "definirClasseSubstituicaoPaginaBitR1BitMIndefinidoTest: " )
        processo = Processo()
        segmento = Segmento()
        classeEsperada = -1
        processo = Processo()
        processo.bitR = 1
        processo.bitM = -1

        segmento = Segmento()

        # Execução
        classeEsperada = -1

        if( processo.bitR  == 0 and processo.bitM == 0 ):
            classeEsperada = 0

        elif( processo.bitR  == 0 and processo.bitM == 1 ):
            classeEsperada = 1

        elif( processo.bitR  == 1 and processo.bitM == 0 ):
            classeEsperada = 2

        elif( processo.bitR  == 1 and processo.bitM == 1 ):
            classeEsperada = 3

        else:
            classeEsperada = -1

        segmento.processo = processo

        # Validação
        segmento.definirClasseSubstituicaoPagina()
        if( classeEsperada == segmento.classeSubstituicao ):
            print( "Esperado: {} == Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )
        else:
            print( "Esperado: {} != Retornado: {}".format( classeEsperada, segmento.classeSubstituicao ) )