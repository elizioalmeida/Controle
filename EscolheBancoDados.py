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
    #self.vTree = self.builder.add_from_file("escolhe.glade") -- não achei mais
    self.w_BD = self.builder.add_from_file("escolheBD.glade")
    
    
    
    
    #---- Glade
    d = self.go("w_dialog")
     
    #----handlers
    self.handlers = {"onDeleteWindow": sys.exit,
    "on_w_dialog_response": self.resp,
    }

    d.show()
    print '--fez o show do dialogo'
    

def escolhe(self):
    
    print 'Estou em escolhe =='
    #----iniciar
    #self.builder = gtk.Builder()
    self.go = self.builder.get_object
    self.w_BD = self.builder.add_from_file("escolheBD.glade")

    
    #---- Glade
    d = self.go("w_dialog")
    
    
    d.show()
    print 'fez o show do dialogo >>>>'
     
    #----handlers
    self.handlers = {"onDeleteWindow": sys.exit,
    #"on_button1_clicked": self.resp,
    #"on_w_dialog_response": self.resp,
    }

    
        
    #--------Banco Consolida
    self.consolida = sqlite3.connect("Consolida.db")
    self.consolidaconecta = self.consolida.cursor()

    #self.storeCombo_BD = self.go("liststore1")

    store = self.go('liststore_d1')
    store.clear()
    self.consolidaconecta.execute("""
    SELECT mesano, DBase, Status
    FROM TabelaMensal
    ORDER BY mesano
				""" )
    self.consolida.commit()
    table = self.consolidaconecta.fetchall()

    for row in table:
	store.append([ row[0], row[1], row[2] ])
	print 'Arquivos', row[0], row[1], row[2]
	#combo.append_text(str(row[1]))


   

    #combo = gtk.ComboBox(store)
    #combo.set_active(0)
    #combo = gtk.combo_box_new_text()
    #label = gtk.Label('Escolha o mês')
    
    
    


    resp(self)
    print '$$$$$$$$$$$$$$$$$$ to aqui'


    d.destroy()



    label = gtk.Label("Escolha o Mês")
    d = gtk.Dialog("Falta um Mês.",
		       None,
		       gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
		       (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT,
			gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
    d.vbox.pack_start(label)
    label.show()

    
    
    escolhe_BKP(self)
    
    
def resp(self):
    
    print ' resp' 
    
    
    
def escolhe_BKP(self):

    print ' Estou em escolhe'
    #--------Banco Consolida
    self.consolida = sqlite3.connect("Consolida.db")
    self.consolidaconecta = self.consolida.cursor()

    self.w_BD = self.builder.add_from_file("escolhe_BD.glade")
    
    w_BD = self.go('w_BD')
    w_BD.show()
    #self.storeCombo_BD = self.go("liststore1")
    print ' messagem = combo' 
    
    
    label = gtk.Label("Escolha o Mês")
    dialog = gtk.Dialog("Falta um Mês.",
		       None,
		       gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
		       (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT,
			gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
    dialog.vbox.pack_start(label)
    label.show()
    
    #checkbox = gtk.CheckButton("Useless checkbox")
    #dialog.action_area.pack_end(checkbox)
    #checkbox.show()

    #dialog.action_area.add(teste)
    #teste.show()

    #combo = gtk.combo_box_new_text()
    
    
    store = self.go('liststore_d1')
    store.clear()
    self.consolidaconecta.execute("""
    SELECT mesano, DBase, Status
    FROM TabelaMensal
    ORDER BY mesano
				""" )
    self.consolida.commit()
    table = self.consolidaconecta.fetchall()
    
    combo = gtk.ComboBox(store)
    #combo.append_text('hello')
    #combo.append_text('world')
    #combo.set_active(0)
    
    combo.set_active(0)
    
    combo = gtk.combo_box_new_text()
    BD = 'nada'
    for row in table:
	store.append([ row[0], row[1], row[2] ])
	print 'Arquivos', row[0], row[1], row[2]
	combo.append_text(str(row[1]))
	
	if row[1] == 'Junho15':
	    BD = row[0] 
	    
	    print ' Banco de Dados     /' , BD
	    break

    return "teste"
    
    combo.set_active(0)
    
    #dialog.action_area.add(combo)
    dialog.vbox.pack_start(combo)
    combo.show()

	
    #a = BD()
    #print a, ' recebeu' 
		 
    #store == erro para eu voltar aqui # fazer um gtk.dialog
    #return store

	
    response = dialog.run()
    
    if response == gtk.RESPONSE_ACCEPT:
	print ' apertei o OK'
	
   
	
    dialog.destroy()
    
    

