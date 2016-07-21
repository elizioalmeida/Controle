#!/usr/bin/env python
# coding:utf-8
# -*- coding: utf_8 -*-


import os

import sys

import pygtk
pygtk.require("2.0")


import gtk
import gtk.glade
import sqlite3
import gobject
import locale
import datetime

from locale import setlocale, currency as moeda, LC_ALL
import exceptions
import re 



def __init__(self):

    self.builder = gtk.Builder()
    self.go = self.builder.get_object
    self.vTree = self.builder.add_from_file("main.glade")


def paginaNB( selfm ):

    # verifica qual a aba do notebook esta aberta
    Main = selfm.nbMain.get_current_page()
    Cad = selfm.nbCadastro.get_current_page()
    Rat = selfm.nbRateio.get_current_page()
    #Consolidar não tem notebook
    #Relatório ainda não fiz.    
	
    print 'Main = ', Main
    print 'Cad = ', Cad
    print 'Rat = ', Rat
    
    return (Main, Cad, Rat) 
    


def Adic(  a, selfm ):
    print ' iniciando o Addicionar', a 
    print ' {{{{{{{{{{{{{{{{{{{{{{{{{{{ = self =', selfm
   
    # verifica qual a aba do notebook esta aberta
    
    (Main, Cad, Rat) = paginaNB(selfm)
    
    if Main == 0: #Cadastro
	if Cad == 0:
	    selfm.AdicionarCusto()
	elif Cad == 1:
	    selfm.AdicionarRecurso()
	elif Cad == 2:
	    selfm.AdicionarProjeto()
	elif Cad == -1:
	    print 'não tem página nenhuma'

    elif Main == 1: #Rateio
	if Rat == 0:
	    selfm.AdicionarRateio(a)# (a) é o botão clicado
	elif Rat == 1:
	    selfm.AdicionaRateioProjeto(a)
	elif Rat == 2:
	    selfm.AdicionarCustoProjeto(a)

    elif Main == 2: #Consolidar
	print ' acho que valia a pena fazer uma menssagem.'
	selfm.AdicionarBD()


	
		    
		    
