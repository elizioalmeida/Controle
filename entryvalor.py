#!/usr/bin/env python
# coding:utf-8
# -*- coding: utf_8 -*-

import os
import sys
try:
    import pygtk
    pygtk.require("2.0")
except:
    pass

import gtk
import gtk.glade
import sqlite3
import gobject
import locale
import datetime

from locale import setlocale, currency as moeda, LC_ALL
import exceptions
import re 



def EntryValor(self, a1):
    print ' ENTRYVALOR ', self, a1
    
    #---- cores
    self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("red"))
    self.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("blue"))
    self.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse("lavender"))
    self.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("green"))
    
    #---- limpa entry
    #self.mask = 9 # sera que preciso???
    newlimp = [""]
    limpar=self.get_text()
    print 'limpar = ', limpar
    lim = re.compile(r'[\d,]')
    limpar = list(limpar)
    print limpar

    for l in limpar:
        print l
        if lim.match(l):
            newlimp.append(l)

    print ' newlimp ====>', newlimp
    newlimp = ''.join(newlimp)
    print newlimp         
            
    self.set_text(newlimp)

def entryPast(self, *args):
	self.n = 1
	print 'ENTRYPAST ----- com enter'
	print 'a1 = ', self
	valor = self.get_text()
	if valor[:2] == 'R$':
		try:
			valor = locale.atof(valor[2:])
			self.set_text(locale.currency((valor), grouping=True))
		except:
			print 'aviso loop R$' 
			dialogoNumero(self)
	elif valor == "":
		print ' aviso loop de vazio'
		if self.n == 1:
			dialogoNumero(self)
		else:
			pass
			
	else:
		valor = locale.atof(valor)
		self.set_text(locale.currency((valor), grouping=True))


    



def filtro (self, ent, a2, a3):
	print ' FILTRO '
	print ' self = ', self
	print ' args a1 = ', ent
	print ent
	num = re.compile(r'[\d]')
	virgula = re.compile(r'[\,]')	
	
	if num.match(ent):
		print num.findall(ent), 'foi validado no entryvalor' # numeros digitados vai dando looper
		#------------ verifica posição na mascara
		

	elif virgula.match(ent):
		print virgula.findall(ent), ' foi validado a virgula'
	else:
		ent = ""
		print 'não foi validado no entryvalor - chamar um aviso '
	
	self.texto = self.get_text()
	print ' texto do FILTRO1 = ', self.texto
	
	#mascara(self, ent)
	
		
def mascara(self, ent):
	print ' MASCARA ', self
	print 'entrada' , ent
	mask = 9
	print mask 
	print ' texto do MASCARA = ', self.texto
	_len=int(len(self.texto))
	print ' len do texto = ', _len
	if _len < (mask - 2):
		print ' esta dentro = ', _len , mask 
	else:
		print ' passou = ', _len , mask


#------- DIALOGOS		
def dialogoNumero( self ):
	
	print ' self = '
	parent = None
	md = gtk.MessageDialog(parent,
		gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_WARNING,
        gtk.BUTTONS_CLOSE, "O valor tem que ser numérico.")

	md.format_secondary_text('Valor fora dos parâmetros.')
	md.set_title('Valor Rateado')
	response = md.run()

	if response == gtk.RESPONSE_CLOSE:
		self.n = 0

        md.destroy()

	
	
	
	

'''
#------- FINAL        

if __name__ == "__main__":
    hwg = principal()
    gtk.main()
'''
