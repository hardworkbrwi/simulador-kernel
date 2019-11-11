#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#statusSegmento.py

from enum import Enum

class StatusSegmento( Enum ):
    '''	
	Enum que define se um segmento está ocupado ou livre
	'''
    LIVRE = 0
    ALOCADO = 1