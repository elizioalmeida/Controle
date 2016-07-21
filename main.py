#!/usr/bin/env python
# coding:utf-8
# -*- coding: utf_8 -*-

##º°

import os
import sys

import pygtk
pygtk.require("2.0")



import gtk
print  gtk.pygtk_version
import gtk.glade
import sqlite3
import gobject
import locale
import datetime

from locale import setlocale, currency as moeda, LC_ALL
import exceptions

import entryvalor
from entryvalor import EntryValor, filtro, entryPast, dialogoNumero

import Consolidado
from Consolidado import ListProjCons,  sel_row_mesano, copiaarquivo, edita_status


import Addic
from Addic import Adic , paginaNB # não preciso de Adic
from Addic import*
print ' MOVEU???'


#import EscolheBancoDados
from EscolheBancoDados import escolhe, resp


import shutil

import pango

from dialogo import getText, dialogoAviso

# teste

class principal:
    """Programa Principal"""
    def __init__(self):
    
        self.builder = gtk.Builder()
        self.go = self.builder.get_object
        self.vTree = self.builder.add_from_file("main.glade")
        #self.P = testemain.Projeto()

        #----------
        #---- Glade
        self.w = self.go('w_principal')

        self.nbMain = self.go("nbMain")
        self.nbCadastro = self.go('nbCadastro')
        self.nbRateio = self.go('nbRateio')
        self.nbConsolidado = self.go('nbConsolidado')
        
	self.combobox1 = self.go('combobox1')
        self.combobox2 = self.go('combobox2')
        self.combobox3 = self.go('combobox3')
        
	self.twListCusto = self.go("twListCusto")
	self.twListRecurso = self.go("twListRecurso")
	self.twListProjeto = self.go("twListProjeto")
        self.twListCusto1 = self.go("twListCusto1")
	
        self.toolbar1 = self.go("toolbar1")
        self.vbox1 = self.go("vbox")
        self.crc_cus = self.go("cellrendererClasse")
        self.crc_rec = self.go("cellrendererSituacao")
        self.storeCombo_cus = self.go("liststore4")
        self.storeCombo_rec = self.go("liststore5")
	self.crc_cons = self.go("cellrendererStatus")
	self.storeCombo_cons = self.go("liststore19")
        self.enCusto = self.go("enCusto")
        self.enValorRat = self.go("enValorRat")
        self.enTotRat = self.go("enTotRat")
        self.enDiferenca = self.go("enDiferenca")
        self.enCustoRateio = self.go("enCustoRateio")
        self.lblCusto = self.go("lblCusto")
	#================
	self.AdicionarCad = self.go("AdicionarCad")
	self.ApagarCad = self.go("ApagarCad")
	self.EditarCad = self.go("EditarCad") # preciso do botão editar?
	self.ConsolidarCad = self.go("ConsolidarCad")
	self.CopiarCad = self.go("CopiarCad")
	self.SairCad = self.go("SairCad")
	#----------------
	self.AdicionarRat = self.go("AdicionarRat")
	self.ApagarRat = self.go("ApagarRat")
	self.EditarRat = self.go("EditarRat")
	self.ConsolidarRat = self.go("ConsolidarRat")
	self.CopiarRat = self.go("CopiarRat")
	self.SairRat = self.go("SairRat")
	#----------------
	self.AdicionarCon = self.go("AdicionarCon")
	self.ApagarCon = self.go("ApagarCon")
        self.EditarCon = self.go("EditarCon")
	self.ConsolidarCon = self.go("ConsolidarCon")
	self.CopiarCon = self.go("CopiarCon")
	self.SairCon = self.go("SairCon")
	#----------------
	self.SairRel = self.go("SairRel")
	
	
	
	
	
        self.cellrendererNome1 = self.go('cellrendererNome1')
        self.twRatCus = self.go('twRatCus')
        self.enTotalRecurso = self.go('enTotalRecurso')
        self.twListRecurso2 = self.go('twListRecurso2')
        self.enRecurso = self.go('enRecurso')
        self.enValorRat1 = self.go("enValorRat1")
        self.cellrendererRateio = self.go("cellrendererRateio")
        self.enTotalRecurso1 = self.go('enTotalRecurso1')
        self.enTotRat1 = self.go("enTotRat1")
        self.enDiferenca1 = self.go("enDiferenca1")
        self.enRateioProj = self.go("enRateioProj")
        self.twRatPro = self.go("twRatPro")
        self.twListCusto2 = self.go("twListCusto2")
        self.enCusto1 = self.go("enCusto1")
        self.enTotalRecurso2 = self.go("enTotalRecurso2")
        self.enTotRat2 = self.go("enTotRat2")
        self.enCustoProj = self.go("enCustoProj")
        self.enDiferenca2 = self.go("enDiferenca2")
        self.enValorRat2 = self.go("enValorRat2")
        self.twCusPro = self.go("twCusPro")

	self.vbox2 = self.go("vbox2")
	
	
	
	#----------
	#----handlers
        self.handlers = {"onDeleteWindow": sys.exit,
			#---------
			
			
                        "on_hbCusto_focus": self.ListCusto,
                        "on_hbox3_focus": self.ListRecurso,
                        "on_hbox4_focus": self.ListProjeto,
			#----------
			"on_cellrendererClasse_changed": self.combo_cus,
                        "on_cellrendererSituacao_changed": self.combo_rec,
                        "on_cellrendererSituacao_edited": self.combo_rec,
			#-------
		
			#==========
			#"on_nbMain_change_current_page": self.VerPag,
			"on_nbMain_switch_page": self.VerPag,
			"on_nbCadastro_switch_page": self.VerPag,
			"on_nbRateio_switch_page": self.VerPag,
                        #----EDITA CUSTO
                        "on_cellrendererName_edited": self.edita_name_cus,
                        "on_cellrendererClasse_edited": self.edita_classe,
                        "on_cellrendererValorCus_edited": self.edita_valor_cus,
                        #----EDITA RECURSO
                        "on_cellrendererNome_edited": self.edita_nome,
                        "on_cellrendererValorRec_edited": self.edita_valor_rec,
                        "on_cellrendererSituacao_edited": self.edita_situacao,
                        "on_cellrendererAdmissao_edited": self.edita_admissao,
                        #----EDITA PROJETO
                        "on_cellrendererProjeto_edited": self.edita_pro,
                        #"on_cellrendererProjeto_edited": self.P.e,
                        "on_cellrendererCliente_edited": self.edita_cli,
                        "on_cellrendererDataInicio_edited": self.edita_dini,
                        "on_cellrendererDataFim_edited": self.edita_dfim,
                        "on_cellrendererValor_edited": self.edita_valor,
                        #----EDITA RATEIO
                        "on_cellrendererRateio_edited": self.edita_valor_rat,
                        #-----RATEIO
                        "on_combobox1_changed": self.ListCusRec,
                        #"on_twListCusto1_cursor_changed": self.ListCusRec2, #ver se pode ser o s/2 APAGAR
                        "on_twListCusto1_cursor_changed": self.ListRecCus,
                        "on_enValorRat_activate": self.mainEntryPast,
                        "on_enValorRat_button_press_event": EntryValor,
                        "on_enValorRat_focus": EntryValor,
                        "on_enValorRat_insert_text": filtro,
                        #-----RATEIOPROJETO
                        "on_twListRecurso2_cursor_changed": self.ListProRec,
                        "on_enValorRat1_activate": self.mainEntryPast,
                        "on_combobox2_changed": self.ListRecPro,
                        "on_cellrendererRateio2_edited": self.edita_valor_rat_pro,
                        #--------RATEIOCUSTOPROJETO
                        "on_combobox3_changed": self.ListCusPro,
                        "on_twListCusto2_cursor_changed":self.ListProCus,
                        "on_enValorRat2_activate": self.mainEntryPast,
			#"on_treeviewcolumn2_clicked": self.teste,
			
                         }
        self.builder.connect_signals(self.handlers)
	
	
	# -------- usar para fazer testes. 
	#self.h_twListRecurso2_cursor_changed = self.twListRecurso2.connect("cursor_changed", self.testando )
	#-------------------------------
	
	
	self.h_twListCusto_cursor_changed = self.twListCusto.connect("cursor_changed", self.verApagar)
	self.h_twListRecurso_cursor_changed = self.twListRecurso.connect("cursor_changed", self.verApagar)
	self.h_twListProjeto_cursor_changed = self.twListProjeto.connect("cursor_changed", self.verApagar)
	self.h_twRatCus_cursor_changed = self.twRatCus.connect("cursor_changed", self.verApagar) # parei aqui
	self.h_twRatPro_cursor_changed = self.twRatPro.connect("cursor_changed", self.verApagar)
	self.h_twCusPro_cursor_changed = self.twCusPro.connect("cursor_changed", self.verApagar)
	
	
	#------------BOTÕES
	self.h_AdicionarCad_clicked = self.AdicionarCad.connect("clicked", Adic, self)
	self.h_AdicionarRat_clicked = self.AdicionarRat.connect("clicked", Adic, self)
	self.h_AdicionarCon_clicked = self.AdicionarCon.connect("clicked", Adic, self) 
	
	self.h_ApagarCad_clicked = self.ApagarCad.connect("clicked", self.Apagar)
	self.h_ApagarRat_clicked = self.ApagarRat.connect("clicked", self.Apagar)
	
	self.h_SairCad_clicked = self.SairCad.connect("clicked", self.close_window)
	self.h_SairRat_clicked = self.SairRat.connect("clicked", self.close_window)
	self.h_SairCon_clicked = self.SairCon.connect("clicked", self.close_window)
	self.h_SairRel_clicked = self.SairRel.connect("clicked", self.close_window)
	
	
	
	
	#--------CONSOLIDADO
	self.twConsolidar = self.go("twConsolidar")
	self.cellrendererName3 = self.go("cellrendererName3")
	#self.h_twConsolidar_cursor_changed = self.twConsolidar.connect("cursor_changed", self.ListProView1)
	self.h_twConsolidar_cursor_changed = self.twConsolidar.connect("cursor_changed", self.verApagar)
	self.cellrendererStatus = self.go("cellrendererStatus")
	#self.h_cellrendererStatus_changed = self.cellrendererStatus.connect("changed", self._BancoEmUso) # por que????? ( acho que não preciso )
	self.h_cellrendererStatus_edited = self.cellrendererStatus.connect("edited", edita_status, self)
	self.h_ConsolidarCon_clicked = self.ConsolidarCon.connect("clicked", copiaarquivo, self) # mudei
	self.h_cellrendererName3_edited = self.cellrendererName3.connect("edited", self.edita_DB_name)
	
	#self.h_AdicionarCon_clicked = self.AdicionarCon.connect("clicked", self.Adicionar) # por que esta indo para o Adicionar?
	
	
	
	#self.h_cellrendererStatus_editing_started = self.cellrendererStatus.connect("editing_started", self.combo_consolidado)
	#self.h_cellrendererStatus_editing_canceled = self.cellrendererStatus.connect("editing_canceled", self.teste)
	#self.h_cellrendererStatus_editing_started = self.cellrendererStatus.connect("editing_started", self.teste)
	#self.h_liststore19_row_changed = self.storeCombo_cons.connect("row_changed", self._BancoEmUso)
	
	
	#----------
        #---------- processo
        self.w.show()
        self.w.connect("destroy", gtk.main_quit)
	#self.w.connect('destroy', lambda wl: gtk.main_quit())
	
	print '{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{', self
	#----------
	# ---- abre a aba Consolidar
	
	
	
	#self.nbMain.set_current_page(2) #?
	
	self.nbMain.set_show_tabs(False) #?
	
	self.nbMain.set_show_tabs(True) #?
	
	
	
	
	
	#----------	
	#--------Banco Consolida
	self.consolida = sqlite3.connect("Consolida.db")
	self.consolidaconecta = self.consolida.cursor()
	
	
        #--------
        # Cores
        self.w.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("light steel blue"))
        self.toolbar1.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("red"))
        self.nbCadastro.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("light steel blue"))
        self.nbRateio.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("lemon chiffon"))
        #self.vbox1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("light steel blue"))
        #self.lblCusto.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("mediumblue"))
        self.enCustoRateio.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("mediumblue"))
        self.enCustoRateio.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse("lemon chiffon"))
        self.combobox1.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse("lemon chiffon"))
        self.cellrendererRateio.set_property('cell-background', 'yellow')


        #------------
        # Pango - Fontes
        fontdesc = pango.FontDescription("TlwgMono, bold 11 ")
        #self.lblCusto.modify_font(fontdesc)
        self.enCustoRateio.modify_font(fontdesc)
	
	
	
	#----------
	# ----- ver primeiro se tem banco em uso
	
	#self.begin()
	
	
    #def begin(self):
	
	print '1.0 primeiro do primeiro '
	
	
	
	#self.nbMain.set_current_page(2) #?
	
	#self.nbMain.set_show_tabs(False)
	
	self.nbMain.set_show_tabs(True) #?
	
	
	print 'ver primeiro se tem banco em uso'
	BD_ = self._BancoEmUso()
	
	print 'testando', BD_
	
	
	
	'''
	if BD_ == '':
	    self.begin()
	    
	else:
	    self.inicia(BD_)
	
	#input('nnn')
	
	'''
	
	#self.inicia(BD_)
    '''
    def comboChanged(self, cell, path, newiter):
	print ' ÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇÇ' 
	e = gtk.gdk.Event(gtk.gdk.FOCUS_CHANGE)
	e.window = self.twConsolidar.window
	e.send_event = True
	e.in_ = True
	print self.w.emit('focus-out-event', e)


    vale a pena depois estudar sobre GDK
    '''
    def teste(self):
	print 'testando    ^^^^^^^^^^^^^^^^^^^^^^^^^^^'
	raw-input('testando    ^^^^^^^^^^^^^^^^^^^^^^^^^^^')
	
	

    def inicia(self, DB_): # inicia todos os treeview.
	print 'I N I C I A ' , DB_
	
	self.con = sqlite3.connect(DB_)
	self.conecta = self.con.cursor()
	self.con.execute('PRAGMA foreign_keys=ON')
	self.con.execute('PRAGMA encoding="UTF-8";')
	
	#-------
        # Escrever acentos e etc.
	try:
	    self.con.text_factory = str
	    print ' text_factory OK'
	except:
	    print ' text_factory NÃO OK'
	    pass
	
	#-------
	# Refaz as tabs
	print 'inicia com o show das tabs '
	self.nbMain.set_show_tabs(True)
	# testando self.nbMain.set_current_page(0)
	print 'iniciou ???? a com o show das tabs ???? '
	
	#------
	# Inicia os processos 
	#Addic.Adic(self, DB_) == ver porque estava chamando esta def;;;;;;
	self.ListCusto()
        self.ListCusto1()
        self.ListCusto2()
        self.ListRecurso()
        self.ListProjeto()
        #self.ListCusRec() #
	
        self.limpaValorEntry()
        self.limpaValorEntryRat1()

        self.ListRec()

        self.combo_cus()
        self.combo_rec()
        self.combo1()
        self.combo2()
	self.combo_consolidado()
	

    def _BancoEmUso(self, *a):
	print 'Banco em Uso ()()()()()()()'
	
	(table, store) = self.ListBD()
	
	print 'table = ', table
	print 'store = ', store
	
	
	'''
	#--------Banco Consolida
	self.consolida = sqlite3.connect("Consolida.db")
	self.consolidaconecta = self.consolida.cursor()
	
	self.consolidaconecta.execute("""
        SELECT mesano, DBase, Status 
        FROM TabelaMensal
                                        """ )
        self.consolida.commit()
        table = self.consolidaconecta.fetchall()
	store = self.go('liststore17')
	
	'''
	
	
	#store.clear()
	#st = [1,1]
	st = []
	DB = ''
	
	
	for row in table:
	    #store1.append([ row[0], row[1], row[2] ])
	    if row[2] == 'Em Uso':
		DB = row[1] + '.db'
		
	    st.append( row[0] )
	    st.append( row[1] )
	    st.append( row[2] )
	    
	    
	qtU = st.count('Em Uso')
	print 'qtU :', qtU, ' ===>> ', st
	
	
	if qtU == 1 :
	    print 'MUITO BEM, bem bem'
	    print ' deu certo? ', row[2], '   ', DB	    
	    
	    
	    self.inicia(DB)
	    
	    #return(r1)
	
	    
	    
	else:
	    print 'messege box.'
	    
	    if qtU == 0: 
		t1 = "Necessário ao menos um arquivo com status 'Em Uso'"
	    else:
		t1 = "Pro favor modifique o status para ter somente um arquivo para em uso"
		
	    t2 = "Modifique o campo na coluna Status"
	    t3 = 'Escolha um Arquivo'
	    
	    self.w.set_sensitive(False)
	    self.nbMain.set_show_tabs(False)
	    self.nbMain.set_current_page(2)
	    
	    
	    dialogoAviso (self, t1, t2 , t3)
	    
	    
	    print ' FOI e VOLTOU '
		
		
	    self.combo_consolidado(self)
		
		
	    self.w.set_sensitive(True)
		
	    return 'Mude_BD.db'
		
	    pass
	    
		
	#raw_input("PRESS ENTER TO CONTINUE. aqui")
	
	print ' passou ????? '
	    
	   
	    

#------ LABEL
    def labelCusto(self, a1, a2):
        print 'teste====>',  a1, self, a2

        a2.set(a1)


#------ ENTRY


    def limpaValorEntry(self):
	print ' limpaValorEntry ========'
        self.enValorRat.set_text("R$ ")
    def limpaValorEntryRat1(self):
        self.enValorRat1.set_text("R$ ")
    def limpaValorEntryRat2(self):
        self.enValorRat2.set_text("R$ ")

    def mainEntryPast(self, a2):
        print 'self do main que esta mandando', self, a2
        entryPast(a2)
        print 'self para botao =====' , self
        self.btnSensitive()

    
    def verApagar(self, a):

        print 'teste focus em ListCusto'
        print 'a = ', a, 'self ', self
	
	# ===== busca página.
	(Main, Cad, Rat) = paginaNB(self)
	
	if Main == 0:	    	
	    try:
		print 'estou no TRY Cadastro'
	     
		selection = a.get_selection()
		selection.set_mode(gtk.SELECTION_SINGLE)
		tree_model, tree_iter = selection.get_selected()
		b = tree_model.get_value(tree_iter,  0 )
		
		print b
		self.ApagarCad.set_sensitive(True)
		print ' TRY'
	    except:
		self.ApagarCad.set_sensitive(False)
		print ' EXCEPT'
	    print '$$$$$$$$$$$ terminou o teste Cadastro'
	
	elif Main == 1:
	    try:
		print 'estou no TRY Rateio'
	     
		selection = a.get_selection()
		selection.set_mode(gtk.SELECTION_SINGLE)
		tree_model, tree_iter = selection.get_selected()
		b = tree_model.get_value(tree_iter,  0 )
		
		print b
		self.ApagarRat.set_sensitive(True)
		print ' TRY'
	    except:
		self.ApagarRat.set_sensitive(False)
		print ' EXCEPT'
	    print '$$$$$$$$$$$ terminou o teste Rateio'
	
	elif Main ==2:
	    try:
		print 'estou no TRY Consolidado'
		selection = a.get_selection()
		selection.set_mode(gtk.SELECTION_SINGLE)
		tree_model, tree_iter = selection.get_selected()
		b = tree_model.get_value(tree_iter,  0 )
		
		print b
		self.ApagarCon.set_sensitive(True)
		#self.AdicionarCon.set_sensitive(True)
		self.CopiarCon.set_sensitive(False)
		
		
	    except:
		self.ApagarCon.set_sensitive(False)
		#self.AdicionarCon.set_sensitive(False)
		self.CopiarCon.set_sensitive(False)
		print ' EXCEPT do Consolidado'
		
	    print '$$$$$$$$$$$ terminou o teste Consolidado'
	
	
    def btnSensitive(self ):
	
        print 'Verifica botão ======>>>' 
	
	
	
	# ===== busca página.
	(Main, Cad, Rat) = paginaNB(self)
	
	
	if Main == 0: #Cadastro
	    btn = self.AdicionarCad
	    btn.set_sensitive(True)
	    if Cad == 0:
		x=1
	    elif Cad == 1:
		x=1
	    elif Cad == 2:
		x=1
	    
	elif Main == 1: #Rateio
            btn = self.AdicionarRat
	    btn.set_sensitive(False)
	    if Rat == 0:
		valor = self.enValorRat.get_text()
		nome_rat = self.enCusto.get_text()
		combo = self.combobox1.get_active()
	    elif Rat == 1:
		valor = self.enValorRat1.get_text()
		nome_rat = self.enRecurso.get_text()
		combo = self.combobox2.get_active()
	    elif Rat == 2:
		valor = self.enValorRat2.get_text()
		nome_rat = self.enCusto1.get_text()
		combo = self.combobox3.get_active()

	    if valor[:2] == 'R$':
		try :
		    valor = locale.atof(valor[2:])
		except:
		    valor = 0
	    else:
		try :
		    valor = locale.atof(valor)
		except:
		    valor = 0
	    print ' valor = ', valor

	    if nome_rat == "":
		btn.set_sensitive(False)
	    elif valor == 0:
		btn.set_sensitive(False)
	    elif combo < 0:
		btn.set_sensitive(False)
	    else:
		btn.set_sensitive(True)
		return (valor)

	elif Main == 2: #Consolidar
	    btn = self.AdicionarCon
	    btn.set_sensitive(True)
	    
	    (x, selecao) = self.twConsolidar.get_selection().get_selected()
	
	    print 'Liststore =',  x
	    print 'Iter = ', selecao 
	
	    
	    print 'Consolidar  ooo', selecao
	    print 'Main = ', Main
	    print 'Cad = ', Cad
	    print 'Rat = ', Rat
	    
	    
	    
	    #self.btAdicionar2.set_sensitive(True)
	    #self.btEditar.set_sensitive(True)
	    #self.btConsolidar.set_sensitive(False)
	    pass
	
	elif Main == 3: #Relatório
	    print 'falta fazer - Relatório '
	    
	    pass
	    
	    
	print ' repete????', Main, Cad, Rat
	
	
	    
	
	

    def VerPag(self, a1, a2, a3):
	print '  ====== Verifica página do notebook  '
	print '  notebook: ', a1
	print '  a2 = ' , a2
	print '  página: ', a3
        self.limpaValorEntry()
	print ' ===================== 1'
        self.limpaValorEntryRat1()
	print ' ===================== 2'
        self.limpaValorEntryRat2()
	print ' ===================== 3'
        self.btnSensitive()
	self.verApagar(a3)
	#self.btnSensitive1( a1, a3)
	print ' ===================== 4'


#----- COMBOBOX

    def combo_cus(self):
        try:
            self.crc_cus.set_property("editable", True)
            self.crc_cus.set_property("model", self.storeCombo_cus)
            self.crc_cus.set_property("text-column", 0)
            self.crc_cus.set_property("has-entry", True)
            #self.crc.connect("edited", self.on_combo_changed)
        except:
            pass

        self.conecta.execute("""
        SELECT classe
        FROM classes
        ORDER BY classe """)
        self.con.commit()
        table = self.conecta.fetchall()
        #list_combo = ('Direto','Rateado','Custo Indireto','Outro')
        for row in table:
            self.storeCombo_cus.append([row[0]])

    def combo_rec(self):
        try:
            self.crc_rec.set_property("editable", True)
            self.crc_rec.set_property("model", self.storeCombo_rec)
            self.crc_rec.set_property("text-column", 0)
            self.crc_rec.set_property("has-entry", True)# DIFERENTE
            #self.crc.connect("edited", self.on_combo_changed)
        except:
            pass
        self.conecta.execute("""
        SELECT situacao
        FROM situacao
        ORDER BY situacao """)
        self.con.commit()
        table = self.conecta.fetchall()
        for row in table:
            self.storeCombo_rec.append([row[0]])

    def combo1(self): #combobox1
        store = self.go('liststore8')
        store.clear()
        self.conecta.execute("SELECT  row_rec, nome FROM recursos ORDER BY nome")
        self.con.commit()
        table = self.conecta.fetchall()
        for row in table:
            store.append([ row[0], row[1]])

        #self.limpaValorEntry()

    def combo2(self, *args):
        print ' COMBOBOX2 '

        store = self.go('liststore9')
        store.clear()
        self.conecta.execute("SELECT  row_pro, pro_nome FROM projeto ORDER BY pro_nome")
        self.con.commit()
        table = self.conecta.fetchall()
        for row in table:
            store.append([ row[0], row[1]])

        self.ListRecPro()

    def combo3(self, *args):
        print ' COMBOBOX3 '

        store = self.go('liststore9')
        store.clear()
        self.conecta.execute("SELECT  row_pro, pro_nome FROM projeto ORDER BY pro_nome")
        self.con.commit()
        table = self.conecta.fetchall()
        for row in table:
            store.append([ row[0], row[1]])

        self.ListRecPro()
	
	self.verApagar(args)
	
    def combo_consolidado(self, *a):
	print 'combo_consolidado'
        try:
            self.crc_cons.set_property("editable", True)
            #self.crc_cons.set_property("model", self.storeCombo_cons)
	    self.crc_cons.set_property("model", self.storeCombo_cons) #liststore19
            self.crc_cons.set_property("text-column", 0)
            self.crc_cons.set_property("has-entry", True)
            print '((((((((((((((((( NÃO deu pau no combo consolidado '
	    
        except:
	    print '((((((((((((((((( deu pau no combo consolidado '
            pass

	self.storeCombo_cons.clear()
	
        self.consolidaconecta.execute("""
        SELECT status
        FROM status
        ORDER BY status """)
        self.consolida.commit()
        table = self.consolidaconecta.fetchall()
        for row in table:
            self.storeCombo_cons.append([row[0]])
	    
	    print ' row:   ',row[0], 'to aqui !!!!!!'
	
	

#-------SELECIONAR
    def seleciona_row_box(self):
        Rat = self.nbRateio.get_current_page()
        if Rat == 0:
            combo_ = self.combobox1
        elif Rat == 1:
            combo_ = self.combobox2
        elif Rat == 2:
            combo_ = self.combobox3

        try:
            cbx_model = combo_.get_model()
            cbx_iter = combo_.get_active_iter()
            sel_box = cbx_model.get_value(cbx_iter, 0)
            self.limpaValorEntry()
            return sel_box
        except:
            self.limpaValorEntry()
            return 0


    def seleciona_row(self):
        Rat = self.nbRateio.get_current_page()
        if Rat == 0:
            selection_p = self.twListCusto1.get_selection()
        elif Rat == 1:
            selection_p = self.twListRecurso2.get_selection()
        elif Rat == 2:
            selection_p = self.twListCusto2.get_selection()
	
	try:
	    selection_p.set_mode(gtk.SELECTION_SINGLE)
	    tree_model, tree_iter = selection_p.get_selected()
	    sel_cus = tree_model.get_value(tree_iter, 0)
	    cus_name = tree_model.get_value(tree_iter, 1)
	    cus_val = tree_model.get_value(tree_iter, 2)
	    print ' Deu certo'
	    return sel_cus, cus_name, cus_val
	except:
	    print ' deu pau!!!!! '    
	

    def seleciona_row_rateio(self):
        Rat = self.nbRateio.get_current_page()
        if Rat == 0:
            selection_p = self.twRatCus.get_selection()
        elif Rat == 1:
            selection_p = self.twRatPro.get_selection()
        elif Rat == 2:
            selection_p = self.twCusPro.get_selection()

        selection_p.set_mode(gtk.SELECTION_SINGLE)
        tree_model, tree_iter = selection_p.get_selected()

        sel_row = tree_model.get_value(tree_iter, 0)
	
	print ' row selecionada = ', sel_row
	
        #cus_name = tree_model.get_value(tree_iter, 1)
        #cus_val = tree_model.get_value(tree_iter, 2)
        return sel_row


    def Apagar(self, a):
	
	# ===== busca página.
	(Main, Cad, Rat) = paginaNB(self)
	
	print 'def Apagar ', a
        
        if Main == 0:
            if Cad == 0:
                self.ApagarCusto()
            elif Cad == 1:
                self.ApagarRecurso()
            elif Cad == 2:
                self.ApagarProjeto()

        elif Main == 1:
            if Rat == 0:
                self.ApagarRateio()
            elif Rat == 1:
                self.ApagarRateioProjeto()
            elif Rat == 2:
                self.ApagarCustoProjeto()
                



#----------CUSTO
    def ListCusto(self, *a):
        self.conecta.execute("""
        SELECT row_cus, name, classe, valor
        FROM custo
        ORDER BY name
                                """)
        self.con.commit()
        table = self.conecta.fetchall()

        store = self.go('liststore1')
        store.clear()
        for row in table:
            store.append([ row[0], row[1], row[2],
                           locale.currency(row[3], grouping=True) ])

            locale.setlocale(locale.LC_ALL, '' )
	print ' enviando para teste ', a
	
	#self.teste()
	self.verApagar(a)

    def AdicionarCusto(self):
        print 'Adicionar Custo'
        namex = clax = ""
        valx = 0

        self.conecta.execute("""
        INSERT INTO custo(name, classe, valor)
        VALUES(?,?,?)
                                """,(namex, clax, valx))
        self.con.commit()
        self.ListCusto()

    def ApagarCusto(self):
        try :
            row_cus_sel = self.sel_row_cus()
	    
	    t1 = "Confirme (OK) para apagar definitivamente o Custo"
	    t2 = 'Este Custo não poderá ser recuperado.'
	    t3 = 'Apagar Custo'
	    
	    #dialogo = dialogoAviso(self, t1, t2, t3)
	
            parent = None
            md = gtk.MessageDialog(parent,
                    gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                    gtk.BUTTONS_OK_CANCEL, t1)
            md.format_secondary_text(t2)
            md.set_title(t3)
            response = md.run()

            if response == gtk.RESPONSE_OK:
                self.conecta.execute( """
                    DELETE FROM custo WHERE row_cus = ?
                                    """, (row_cus_sel,) )
                self.con.commit()
                md.destroy()
                self.ListCusto()

            elif response == gtk.RESPONSE_CANCEL:
                md.destroy()
	    
        except:
            parent = None
            md = gtk.MessageDialog(parent,
                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                gtk.BUTTONS_CLOSE, "Escolha um Custo a ser apagado")
            md.format_secondary_text('Selecione clicando na linha referente ao Custo.')
            md.set_title('Seleciona o Custo')
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()

    def sel_row_cus (self):
        selection = self.twListCusto.get_selection()
        selection.set_mode(gtk.SELECTION_SINGLE)
        tree_model, tree_iter = selection.get_selected()
        a = tree_model.get_value(tree_iter,  0 )
        return a

    #--------Edição de Custo
    def edita_name_cus(self, a2, a3, valor):# esta modificado
        print self, a2, a3, valor
        row_cus_sel = self.sel_row_cus()
        tb = 'custo'
        query = ("UPDATE "+ tb+ " SET  name = ? WHERE row_cus = ?")
        print query
        self.conecta.execute(query, ( valor, row_cus_sel) )
        self.con.commit()
        self.ListCusto()
	self.ListCusto1()
	self.ListCusto2()

    def edita_classe(self, a2, a3, valor):
        row_cus_sel = self.sel_row_cus()
        self.conecta.execute("""
        UPDATE custo SET  classe = ? WHERE row_cus = ?
                                """, ( valor, row_cus_sel) )
        self.con.commit()
        self.ListCusto()
	self.ListCusto1()
	self.ListCusto2()

    def edita_valor_cus(self, a2, a3, valor):
        if valor[:2] == 'R$':
            valor = locale.atof(valor[2:])
        else:

            try:
                valor = locale.atof(valor)
            except:
                print 'erro de locale'
                dialogoNumero(self)
                self.ListCusto()
                return()
        print ' valor = ', valor
        row_cus_sel = self.sel_row_cus()
        self.conecta.execute("""
        UPDATE custo SET  valor = ? WHERE row_cus = ?
                                """, ( valor, row_cus_sel) )
        self.con.commit()
        self.ListCusto()
	self.ListCusto1()
	self.ListCusto2()

#-------------RECURSO
    def ListRecurso(self, *a):
        print 'inicia liststore_rec'

        self.conecta.execute("""
        SELECT row_rec , nome, valor, situacao, admissao
        FROM recursos
        ORDER BY nome
                                 """)
        self.con.commit()
        table = self.conecta.fetchall()

        store = self.go('liststore2')
        store.clear()
        for row in table:
            store.append([ row[0], row[1],
                           locale.currency((row[2]), grouping=True),
                           row[3], row[4]])

            locale.setlocale(locale.LC_ALL, '' )
        print ' chamando o combo - mas por que?'
        #self.combo1()
	self.verApagar(a)
	



    def AdicionarRecurso(self):
        nomex = sitx = ""
        dadmi = "01/01/01"
        valx = 0

        self.conecta.execute("""
        INSERT INTO recursos(nome, valor, situacao, admissao)
        VALUES(?,?,?,?)
                                """,(nomex, valx, sitx, dadmi))
        self.con.commit()
        self.ListRecurso()
	self.combo1()



    def ApagarRecurso(self):
        try :
            row_rec_sel = self.sel_row_rec()
            print 'row = ', row_rec_sel
            parent = None
            md = gtk.MessageDialog(parent,
                                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                                gtk.BUTTONS_OK_CANCEL, "Confirme (OK) para apagar definitivamente o Recurso")
            md.format_secondary_text('Este Recurso não poderá ser recuperado.')
            md.set_title('Apagar Recurso')
            response = md.run()

            if response == gtk.RESPONSE_OK:
                self.conecta.execute( """
                DELETE FROM recursos WHERE row_rec = ?
                                        """, (row_rec_sel,) )
                self.con.commit()
                md.destroy()
                self.ListRecurso()
		self.combo1()

            elif response == gtk.RESPONSE_CANCEL:
                md.destroy()
        except:
            parent = None
            md = gtk.MessageDialog(parent,
                                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                                gtk.BUTTONS_CLOSE, "Escolha um Recurso a ser apagado")
            md.format_secondary_text('Selecione clicando na linha referente ao Recurso.')
            md.set_title('Seleciona o Recurso')
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()

    def sel_row_rec (self):
        selection = self.twListRecurso.get_selection()
        selection.set_mode(gtk.SELECTION_SINGLE)
        tree_model, tree_iter = selection.get_selected()
        a = tree_model.get_value(tree_iter,  0 )
        return a

    # ---- Edição de Recursos.
    def edita_nome(self, a2, a3, valor):
        row_rec_sel = self.sel_row_rec()
        self.conecta.execute("""
        UPDATE recursos SET  nome = ? WHERE row_rec = ?
                                """, ( valor, row_rec_sel) )
        self.con.commit()
        self.ListRecurso()
        self.combo1()

    def edita_valor_rec(self, a2, a3, valor):
        if valor[:2] == 'R$':
            valor = locale.atof(valor[2:])
        else:
            valor = locale.atof(valor)

        row_rec_sel = self.sel_row_rec()
        self.conecta.execute("""
        UPDATE recursos SET  valor = ? WHERE row_rec = ?
                                """, ( valor, row_rec_sel) )
        self.con.commit()
        self.ListRecurso()
	self.combo1()

    def edita_situacao(self, a2, a3, valor):
        row_rec_sel = self.sel_row_rec()
        self.conecta.execute("""
        UPDATE recursos SET  situacao = ? WHERE row_rec = ?
                                """, ( valor, row_rec_sel) )
        self.con.commit()
        self.ListRecurso()
	self.combo1()
    def edita_admissao(self, a2, a3, valor):
        row_rec_sel = self.sel_row_rec()
        self.conecta.execute("""
        UPDATE recursos SET  admissao = ? WHERE row_rec = ?
                                """, ( valor, row_rec_sel) )
        self.con.commit()
        self.ListRecurso()
	self.combo1()




#--------------PROJETO
    def ListProjeto(self, *a):
        self.conecta.execute("""
        SELECT row_pro, pro_nome, cliente, datainicio, datafinal, valor
        FROM projeto
        ORDER BY pro_nome
                                """)
        self.con.commit()
        table = self.conecta.fetchall()

        store = self.go('liststore3')
        store.clear()
        for row in table:
            store.append([row[0], row[1], row[2], row[3], row[4],
                          locale.currency((row[5]), grouping=True)])

            locale.setlocale(locale.LC_ALL, '' )

            today = datetime.date.today()
            data= str( today.strftime(' %d/ %m/ %Y'))

        print 'liststore refeita'
	self.verApagar(a)
	

    def AdicionarProjeto(self):
        print 'Adicionar Projeto'
        prox = clix = ""
        dinix = dfix = "01/01/01"
        valx = 0

        self.conecta.execute("""
        INSERT INTO projeto(pro_nome, cliente, datainicio, datafinal, valor)
        VALUES(?,?,?,?,?)
                                """,(prox, clix , dinix, dfix , valx))
        self.con.commit()
        self.ListProjeto()

    def ApagarProjeto(self):
        try :
            row_pro_sel = self.sel_row_pro()
            parent = None
            md = gtk.MessageDialog(parent,
                            gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                            gtk.BUTTONS_OK_CANCEL, "Confirme (OK) para apagar definitivamente o Projeto.")
            md.format_secondary_text('Este Projeto não poderá ser recuperado.')
            md.set_title('Apagar Projeto')
            response = md.run()

            if response == gtk.RESPONSE_OK:
                self.conecta.execute( """
                DELETE FROM projeto WHERE row_pro = ?
                                     """, (row_pro_sel,) )
                self.con.commit()
                md.destroy()
                self.ListProjeto()

            elif response == gtk.RESPONSE_CANCEL:
                md.destroy()

        except:
            parent = None
            md = gtk.MessageDialog(parent,
                                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                                gtk.BUTTONS_CLOSE, "Escolha um Projeto a ser apagado")
            md.format_secondary_text('Selecione clicando na linha referente ao Projeto.')
            md.set_title('Seleciona o Projeto')
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()

    def sel_row_pro (self):

        selection = self.twListProjeto.get_selection()
        selection.set_mode(gtk.SELECTION_SINGLE)
        tree_model, tree_iter = selection.get_selected()
        a = tree_model.get_value(tree_iter,  0 )
        return a


    # ---- Edição de Projetos.
    def edita_pro(self, a2, a3, valor):
        row_pro_sel = self.sel_row_pro()
        self.conecta.execute("""
        UPDATE projeto SET  pro_nome = ? WHERE row_pro = ?
                                """, ( valor, row_pro_sel) )
        self.con.commit()
        self.ListProjeto()
    def edita_cli(self, a2, a3, valor):
        row_pro_sel = self.sel_row_pro()
        self.conecta.execute("""
        UPDATE projeto SET  cliente = ? WHERE row_pro = ?
                                """, ( valor, row_pro_sel) )
        self.con.commit()
        self.ListProjeto()
    def edita_dini(self, a2, a3, valor):
        row_pro_sel = self.sel_row_pro()

        self.conecta.execute("""
        UPDATE projeto SET  datainicio = ? WHERE row_pro = ?
                                """, ( valor, row_pro_sel) )
        self.con.commit()
        self.ListProjeto()
    def edita_dfim(self, a2, a3, valor):
        row_pro_sel = self.sel_row_pro()

        self.conecta.execute("""
        UPDATE projeto SET  datafinal = ? WHERE row_pro = ?
                                """, ( valor, row_pro_sel) )
        self.con.commit()
        self.ListProjeto()
    def edita_valor(self, a2, a3, valor):

        if valor[:2] == 'R$':
            valor = locale.atof(valor[2:])
        else:
            valor = locale.atof(valor)

        row_pro_sel = self.sel_row_pro()


        self.conecta.execute("""
        UPDATE projeto SET  valor = ? WHERE row_pro = ?
                                """, ( valor, row_pro_sel) )
        #self.con.commit()
        self.ListProjeto()

#------ CUSTO RECURSO

    def ListCusto1(self, *a): #liststore13
        c = 'Indireto'
        self.conecta.execute("""
        SELECT row_cus, name, valor
        FROM custo
        WHERE classe = ?
        ORDER BY name
                                """, (c,))
        self.con.commit()
        table = self.conecta.fetchall()

        store = self.go('liststore13')
        store.clear()
        for row in table:
            store.append([ row[0], row[1],
                           locale.currency(row[2], grouping=True) ])

            locale.setlocale(locale.LC_ALL, '' )
	    
	

    def ListCusRec(self, *a):

	print 'ListCusRec()  '


        #Recurso Selecionado
        b = self.seleciona_row_box()

        #Custo Slecionado
        self.conecta.execute("""
        SELECT rateio.row_rat , recursos.nome, custo.name, rateio.valor_tot
        FROM rateio, recursos, custo
        WHERE rateio.row_rec = ? and rateio.row_rec = recursos.row_rec and rateio.row_cus = custo.row_cus
                                """, (b,))
        self.con.commit()
        #WHERE rateio.row_rec = recursos.row_rec and rateio.row_cus = custo.row_cus and row_rat = ?
        table = self.conecta.fetchall()

        store = self.go('liststore6')
        store.clear()
        somaRecurso = 0
        for row in table:
            store.append([ row[0], row[1], row[2],
                        locale.currency((row[3]), grouping=True)
                        ])
            locale.setlocale(locale.LC_ALL, '' )
            somaRecurso = somaRecurso + row[3]
	
	self.btnSensitive()
        self.enTotalRecurso.set_text(locale.currency(somaRecurso, grouping = True))
        self.ListRec()
	
	
	self.verApagar(a)

    def ListCusRec2(self, *a1):

        print 'ListCusRec2 '

        selection = self.twListCusto1.get_selection()
        selection.set_mode(gtk.SELECTION_SINGLE)
        tree_model, tree_iter = selection.get_selected()
        a = tree_model.get_value(tree_iter,  0 )# row
        b = tree_model.get_value(tree_iter,  1 )# custo nome
        c = tree_model.get_value(tree_iter,  3 )# valor


        self.enCusto.set_text(b)

        self.limpaValorEntry()
        self.ListRecCus(a, b, c)
        self.btnSensitive()


    def ListRecCus (self,*a): #(self, a1, *b):
	
	print ' TESTE  de lista custo indireto por recurso '
	
	
        self.limpaValorEntry()
	self.btnSensitive()
	
        #(sel_cus, cus_name, cus_val) = self.seleciona_row_cus()
        (sel_cus, cus_name, cus_val) = self.seleciona_row()

	self.enCusto.set_text(cus_name)
	#print ' ESTOU  ListRecCus ===*', self, a1
        print ' ESTOU  ListRecCus ===', sel_cus, cus_name , cus_val


        if cus_val[:2] == 'R$':
            cus_val = locale.atof(cus_val[2:])
        else:
            cus_val = locale.atof(cus_val)


        if sel_cus == "":
            #sel = self.en_row_cus.get_text()
            pass
        else:
            pass

        try:
            self.conecta.execute("""
            SELECT recursos.nome, rateio.valor_tot, rateio.row_cus
            FROM rateio, recursos
            WHERE rateio.row_rec = recursos.row_rec and rateio.row_cus = ?
                                    """, (sel_cus,))
            self.con.commit()
            self.table = self.conecta.fetchall()
            store = self.builder.get_object('liststore7')
            store.clear()
            soma_valor = 0
            for row in self.table:
                store.append([ row[0],
                               locale.currency((row[1]), grouping = True),
                               row[2]])
                print 'OKOKOK'
                soma_valor = soma_valor + row[1]

            #self.entry3.set_text(row[0])
            print 'somaValor = ', soma_valor
            self.enTotRat.set_text(locale.currency(soma_valor, grouping = True))

        except:
                print'deu pau antes do val'

        dif = cus_val - soma_valor
        self.enDiferenca.set_text(locale.currency(dif, grouping = True))
        print ' diferença -------->>' , dif


        self.enCustoRateio.set_text(cus_name)

        #rotulo = self.lblCusto
        #self.labelCusto(a1, rotulo )


        print ' Saindo de ListRecCus '

    def AdicionarRateio(self, btn):
        print ' Adicionar um rateio', self
        # --- valor
        valorx = self.btnSensitive()
        # --- row_rec
        row_recx = self.seleciona_row_box()
        # --- row_cus
        #row_cusx, b, c = self.seleciona_row_cus()
        row_cusx, b, c = self.seleciona_row()

        row_recx = int(row_recx)
        row_cusx = int(row_cusx)
        print ' ROW_REC e ROW_CUS ====', row_recx, row_cusx, type(row_recx), type(row_cusx)

        self.conecta.execute("""
            SELECT recursos.nome, custo.name
            FROM rateio, recursos, custo
            WHERE recursos.row_rec = rateio.row_rec and rateio.row_rec = ?
            and rateio.row_cus = custo.row_cus and rateio.row_cus = ?
                                """, (row_recx, row_cusx,))
        self.con.commit()
        table = self.conecta.fetchall()
        print ' vai testar se tem igual ', table

        if table == []:
            print ' nao nao nao tem igual'
            self.conecta.execute("""
                INSERT INTO rateio(row_rec, row_cus, valor_tot)
                VALUES(?,?,?)
                                    """,(row_recx, row_cusx , valorx))
            self.con.commit()
            self.enValorRat.set_text("")
            self.btnSensitive()
            self.ListCusRec()
        else:
            print ' tem tem tem igual'
            btn.set_sensitive(False)
            for row in table:

                # ------ Aviso
                parent = None
                texto = ('O Rateio de  ' + (row[1]) + ' para o  ' + str( row[0]) +' já existe.')
                md = gtk.MessageDialog(parent,
                    gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                    gtk.BUTTONS_CLOSE, "Rateio duplicado.")
                md.format_secondary_text(texto)
                md.set_title('Entrada Rateio ')
                response = md.run()
                if response == gtk.RESPONSE_CLOSE:
                    md.destroy()

                self.enCusto.set_text("")
                self.limpaValorEntry()
                break


    def sel_row_rat (self):
        selection = self.twRatCus.get_selection()
        selection.set_mode(gtk.SELECTION_SINGLE)
        tree_model, tree_iter = selection.get_selected()
        a = tree_model.get_value(tree_iter,  0 )
        return a


    def edita_valor_rat(self, a2, a3, valor):
        print ' RECEBE ', a2, a3, valor
        if valor[:2] == 'R$':
            valor = locale.atof(valor[2:])
        else:

            try:
                valor = locale.atof(valor)
            except:
                print 'erro de locale'
                dialogoNumero(self)
                self.ListCusto()
                return()
        print ' valor = ', valor
        row_ = self.sel_row_rat()
        print ' row_ ==', row_
        self.conecta.execute("""
        UPDATE rateio SET  valor_tot = ? WHERE row_rat = ?
                                """, ( valor, row_) )
        self.con.commit()
        print ' enviando para list6'
        self.ListCusRec()
        valor = str(valor)

        print ' enviando para list7'
        self.ListRecCus(row_, a2, valor)



    def ApagarRateio(self):
        print ' Apagar Rateio ----->'
	
        try :
            #row_ = self.sel_row_rat()
            row_ = self.seleciona_row_rateio()
            print 'row do rateio == ', row_
            parent = None
            md = gtk.MessageDialog(parent,
                                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                                gtk.BUTTONS_OK_CANCEL, "Confirme (OK) para apagar definitivamente o Rateio")
            md.format_secondary_text('Este Rateio não poderá ser recuperado.')
            md.set_title('Apagar Rateio')
            response = md.run()

            if response == gtk.RESPONSE_OK:

                self.conecta.execute( """
                DELETE FROM rateio WHERE row_rat = ?
                                        """, (row_,) )
                self.con.commit()
                md.destroy()
		self.ApagarRat.set_sensitive(False)
		self.ListCusRec()
                self.ListRecCus()

            elif response == gtk.RESPONSE_CANCEL:
		md.destroy()
		
        except:
            parent = None
            md = gtk.MessageDialog(parent,
                                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                                gtk.BUTTONS_CLOSE, "Escolha um Rateio a ser apagado")
            md.format_secondary_text('Selecione clicando na linha referente ao Rateio.')
            md.set_title('Seleciona Rateio')
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()

#------ RECURSO PROJETO

    def ListRec (self):
        self.conecta.execute("""
            SELECT rateio.row_rec, recursos.nome, SUM (valor_tot)
            FROM rateio, recursos
            WHERE rateio.row_rec = recursos.row_rec
            GROUP BY  rateio.row_rec

                                """)
        self.con.commit()
        table = self.conecta.fetchall()

        store = self.go('liststore10')
        store.clear()
        for row in table:
            store.append([ row[0], row[1],
                           locale.currency(row[2], grouping=True) ])

            locale.setlocale(locale.LC_ALL, '' )


    def ListRecPro (self, *args):
        print ' LISTRECPRO '


        sel = self.seleciona_row_box()
        print ' Projeto selecionado ====', sel

        self.conecta.execute("""
            SELECT rateiorecurso.row_rat_pro, recursos.nome, rateiorecurso.valor
            FROM rateiorecurso, recursos
            WHERE rateiorecurso.row_pro = ? and rateiorecurso.row_rec = recursos.row_rec

                                """, ( sel, ))
        self.con.commit()
        table = self.conecta.fetchall()
        somaValor = 0
        store = self.go('liststore11')
        store.clear()
        for row in table:
            store.append([ row[0], row[1],
                           locale.currency(row[2], grouping=True) ])
            somaValor = somaValor + row[2]
            locale.setlocale(locale.LC_ALL, '' )

        self.enTotalRecurso1.set_text(locale.currency(somaValor, grouping = True))

    def AdicionaRateioProjeto(self, btn):
        print ' adicionando recurso a um projeto'
        valorx = self.btnSensitive()
        print ' Valor ====>>', valorx
        # --- row_pro
        row_prox = self.seleciona_row_box()
        print ' row_pro ====>>', row_prox
        # --- row_rec
        #(row_recx, b, c) = self.Seleciona_Recurso()
        (row_recx, b, c) = self.seleciona_row()
        print ' row_rec ====>>', row_recx
        print b, c

        self.conecta.execute("""
            SELECT projeto.pro_nome, recursos.nome
            FROM projeto, recursos, rateiorecurso
            WHERE rateiorecurso.row_pro = ?
            and rateiorecurso.row_rec = ?
            and recursos.row_rec = rateiorecurso.row_rec
            and projeto.row_pro = rateiorecurso.row_pro

                                """, (row_prox, row_recx,))
        self.con.commit()
        table = self.conecta.fetchall()

        if table == []:
            print ' nao nao nao tem igual', row_recx, row_prox , valorx
            self.conecta.execute("""
                INSERT INTO rateiorecurso(row_rec, row_pro, valor)
                VALUES(?,?,?)
                                    """,(row_recx, row_prox , valorx,))
            self.con.commit()
            self.enValorRat1.set_text("")
            self.btnSensitive()
            self.ListRecPro()
            self.ListProRec()

        else:
            print ' tem tem tem igual'
            btn.set_sensitive(False)
            for row in table:
                print ' listando se valores já existem +++++', table
                btn.set_sensitive(False)

                # ------ Aviso
                parent = None
                texto = ('O Recurso  ' + (row[1]) + ' para o Projeto  ' + str( row[0]) +' já existe.')
                md = gtk.MessageDialog(parent,
                        gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                        gtk.BUTTONS_CLOSE, "Rateio duplicado.")
                md.format_secondary_text(texto)
                md.set_title('Entrada Rateio ')
                response = md.run()
                if response == gtk.RESPONSE_CLOSE:
                        md.destroy()


                self.enRecurso.set_text("")
                self.limpaValorEntryRat1()
                break

    def testando(self,*a):
	raw_input (' testando ')
	 


    def ListProRec(self, *a):
        self.limpaValorEntryRat1()
        self.btnSensitive()


        #(sel_rec, rec_name, rec_val) = self.Seleciona_Recurso()
        (sel_rec, rec_name, rec_val) = self.seleciona_row()
        print 'Dados dos Recursos', sel_rec, rec_name, rec_val
        self.enRecurso.set_text(rec_name)




        #(sel_rec, rec_name, rec_val) = self.Seleciona_Recurso()
        (sel_rec, rec_name, rec_val) = self.seleciona_row()
        self.enRecurso.set_text(rec_name)
        print ' ESTOU  ListProRec ===', sel_rec, rec_name, rec_val


        if rec_val[:2] == 'R$':
            rec_val = locale.atof(rec_val[2:])
        else:
            rec_val = locale.atof(rec_val)


        if sel_rec == "":
            pass
        else:
            pass

        #try:
        self.conecta.execute("""
        SELECT rateiorecurso.row_rec, projeto.pro_nome, rateiorecurso.valor
        FROM rateiorecurso, projeto
        WHERE rateiorecurso.row_rec = ? and rateiorecurso.row_pro = projeto.row_pro
                                """, (sel_rec,))
        self.con.commit()
        table = self.conecta.fetchall()
        store = self.builder.get_object('liststore12')
        store.clear()
        soma_valor = 0
        for row in table:
            store.append([ row[0], row[1],
                           locale.currency((row[2]), grouping = True)])
            print 'OKOKOK ====='
            soma_valor = soma_valor + row[2]

        print 'somaValor ====== ', soma_valor
        self.enTotRat1.set_text(locale.currency(soma_valor, grouping = True))

        #except:
        #        print'deu pau antes do val'

        dif = rec_val - soma_valor
        self.enDiferenca1.set_text(locale.currency(dif, grouping = True))
        print ' diferença -------->>' , dif


        self.enRateioProj.set_text(rec_name)

        #rotulo = self.lblCusto
        #self.labelCusto(a1, rotulo )


        print ' Saindo de ListRecCus '
    
    ''' 
    def sel_row_pro (self):
        selection = self.twRatPro.get_selection()
        selection.set_mode(gtk.SELECTION_SINGLE)
        tree_model, tree_iter = selection.get_selected()
        a = tree_model.get_value(tree_iter,  0 )

        return a
    '''
    
    def edita_valor_rat_pro(self, a2, a3, valor):
        print ' RECEBE ', a2, a3, valor
        if valor[:2] == 'R$':
            valor = locale.atof(valor[2:])
        else:

            try:
                valor = locale.atof(valor)
            except:
                print 'erro de locale'
                dialogoNumero(self)
                self.ListCusto() # para que serve?
                return()
        print ' valor = ', valor
        row_ = self.sel_row_pro()
        print ' row_ ==', row_
        self.conecta.execute("""
        UPDATE rateiorecurso SET  valor = ? WHERE row_rat_pro = ?
                                """, ( valor, row_) )
        self.con.commit()
        print ' enviando para list11'
        self.ListRecPro()
        valor = str(valor)

        print ' enviando para list12'
        self.ListProRec(row_, a2, valor)

    def ApagarRateioProjeto(self):
        print ' Apagar Rateio Projeto----->'
        try :
            # testando row_ = self.sel_row_pro()
            row_ = self.seleciona_row_rateio()
            print 'row do rateio Projeto == sera que deu certo????', row_
            parent = None
            md = gtk.MessageDialog(parent,
                                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                                gtk.BUTTONS_OK_CANCEL, "Confirme (OK) para apagar definitivamente o Rateio referente ao Projeto")
            md.format_secondary_text('Este Rateio deste Projeto não poderá ser recuperado.')
            md.set_title('Apagar Rateio de Projeto')
            response = md.run()

            if response == gtk.RESPONSE_OK:

                self.conecta.execute( """
                DELETE FROM rateiorecurso WHERE row_rat_pro = ?
                                        """, (row_,) )
                self.con.commit()
                md.destroy()
                #self.ListRecPro()
                #self.ListProRec()

            elif response == gtk.RESPONSE_CANCEL:

                md.destroy()
        except:
            parent = None
            md = gtk.MessageDialog(parent,
                                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                                gtk.BUTTONS_CLOSE, "Escolha um Rateio a ser apagado")
            md.format_secondary_text('Selecione clicando na linha referente ao Rateio.')
            md.set_title('Seleciona Rateio Projeto')
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()

        self.ListRecPro()
        self.ListProRec()

#------ CUSTO PROJETO

    def ListCusto2(self, *a): #liststore14
        c = 'Direto'
        self.conecta.execute("""
        SELECT row_cus, name, valor
        FROM custo
        WHERE classe = ?
        ORDER BY name
                                """, (c,))
        self.con.commit()
        table = self.conecta.fetchall()

        store = self.go('liststore14')
        store.clear()
        for row in table:
            store.append([ row[0], row[1],
                           locale.currency(row[2], grouping=True) ])

            locale.setlocale(locale.LC_ALL, '' )
	    
	    

    def ListCusPro (self, *args):
        print ' LIST CUS PRO '


        sel = self.seleciona_row_box()
        print ' Projeto selecionado ====', sel

        self.conecta.execute("""
            SELECT rateiocuspro.row_cus_pro, custo.name, rateiocuspro.valor
            FROM rateiocuspro, custo
            WHERE rateiocuspro.row_pro = ? and rateiocuspro.row_cus = custo.row_cus
                                """, ( sel, ))
        self.con.commit()
        table = self.conecta.fetchall()
        somaValor = 0
        store = self.go('liststore15')
        store.clear()
        for row in table:
            store.append([ row[0], row[1],
                           locale.currency(row[2], grouping=True) ])

            somaValor = somaValor + row[2]
            locale.setlocale(locale.LC_ALL, '' )

        self.enTotalRecurso2.set_text(locale.currency(somaValor, grouping = True))

    def ListProCus(self, *a):
	
        self.limpaValorEntry()
        self.btnSensitive()

        (sel_cus, cus_name, cus_val) = self.seleciona_row()

        self.enCusto1.set_text(cus_name)
        print ' ESTOU  ListProCus ===', sel_cus, cus_name , cus_val, type(cus_name)

        if cus_val[:2] == 'R$':
            cus_val = locale.atof(cus_val[2:])
        else:
            cus_val = locale.atof(cus_val)

        if sel_cus == "":
            #sel = self.en_row_cus.get_text()
            pass
        else:
            pass
        print ' aqui foi 000'
        try:
            self.conecta.execute("""
            SELECT rateiocuspro.row_cus, projeto.pro_nome, rateiocuspro.valor
            FROM projeto, rateiocuspro
            WHERE rateiocuspro.row_pro = projeto.row_pro and rateiocuspro.row_cus = ?
                                    """, (sel_cus,))
            print ' aqui foi 1111'
            self.con.commit()
            self.table = self.conecta.fetchall()
            store = self.builder.get_object('liststore16')
            store.clear()
            soma_valor = 0
            print ' aqui foi'
            for row in self.table:
                store.append([ row[0], row[1],
                               locale.currency((row[2]), grouping = True) ])
                print 'OKOKOK'
                soma_valor = soma_valor + row[2]

            #self.entry3.set_text(row[0])
            print 'somaValor = ', soma_valor
            self.enTotRat2.set_text(locale.currency(soma_valor, grouping = True))

        except:
                print'deu pau antes do val'

        dif = cus_val - soma_valor
        self.enDiferenca2.set_text(locale.currency(dif, grouping = True))
        print ' diferença -------->>' , dif


        self.enCustoProj.set_text(cus_name)

        #rotulo = self.lblCusto
        #self.labelCusto(a1, rotulo )


        print ' Saindo de ListProCus '

    def AdicionarCustoProjeto(self, btn):
        print ' adicionando custo direto a um projeto'
        valorx = self.btnSensitive()
        print ' Valor ====>>', valorx
        # --- row_pro
        row_prox = self.seleciona_row_box()
        print ' row_pro ====>>', row_prox
        (row_cusx, b, c) = self.seleciona_row()
        print ' row_cus ====>>', row_cusx
        print b, c

        self.conecta.execute("""
            SELECT projeto.pro_nome, custo.name
            FROM projeto, custo, rateiocuspro
            WHERE rateiocuspro.row_pro = ?
            and rateiocuspro.row_cus = ?
            and custo.row_cus = rateiocuspro.row_cus
            and projeto.row_pro = rateiocuspro.row_pro

                                """, (row_prox, row_cusx,))
        self.con.commit()
        table = self.conecta.fetchall()

        if table == []:
            print ' nao nao nao tem igual', row_cusx, row_prox , valorx
            self.conecta.execute("""
                INSERT INTO rateiocuspro(row_cus, row_pro, valor)
                VALUES(?,?,?)
                                    """,(row_cusx, row_prox , valorx,))
            self.con.commit()
            self.enValorRat2.set_text("")
            self.btnSensitive()
            self.ListCusPro()
            self.ListProCus()

        else:
            print ' tem tem tem igual'
            btn.set_sensitive(False)
            for row in table:
                print ' listando se valores já existem +++++', table
                btn.set_sensitive(False)

                # ------ Aviso
                parent = None
                texto = ('O Custo  ' + (row[1]) + ' para o Projeto  ' + str( row[0]) +' já existe.')
                md = gtk.MessageDialog(parent,
                        gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                        gtk.BUTTONS_CLOSE, "Custo Direto duplicado.")
                md.format_secondary_text(texto)
                md.set_title('Entrada Rateio Custo Direto ')
                response = md.run()
                if response == gtk.RESPONSE_CLOSE:
                        md.destroy()


                self.enRecurso.set_text("")
                self.limpaValorEntryRat1()
                break

    def ApagarCustoProjeto(self):
        print ' Apagar Custo Projeto----->'
        try :
            #row_ = self.sel_row_pro()
            print ' ESTA PEGANDO A ROW_ ====='
            row_ = self.seleciona_row_rateio()
            print 'row do Custo Projeto == ', row_
            parent = None
            md = gtk.MessageDialog(parent,
                                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                                gtk.BUTTONS_OK_CANCEL, "Confirme (OK) para apagar definitivamente o Rateio referente ao Projeto")
            md.format_secondary_text('Este Rateio - Custo deste Projeto não poderá ser recuperado.')
            md.set_title('Apagar Rateio - Custo de Projeto')
            response = md.run()

            if response == gtk.RESPONSE_OK:

                self.conecta.execute( """
                DELETE FROM rateiocuspro WHERE row_cus_pro = ?
                                        """, (row_,) )
                self.con.commit()
                md.destroy()
                self.ListCusPro()
                self.ListProCus()

            elif response == gtk.RESPONSE_CANCEL:

                md.destroy()
        except:
            parent = None
            md = gtk.MessageDialog(parent,
                                gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION,
                                gtk.BUTTONS_CLOSE, "Escolha um Rateio a ser apagado")
            md.format_secondary_text('Selecione clicando na linha referente ao Rateio.')
            md.set_title('Seleciona Rateio - Custo Projeto')
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()

        self.ListCusPro()
        self.ListProCus()

    
    #------ CONSOLIDADO
    
    def ListBD(self):
    
	print ' ListBD     '
	#--------Banco Consolida
	self.consolida = sqlite3.connect("Consolida.db")
	self.consolidaconecta = self.consolida.cursor()
	
	self.consolidaconecta.execute("""
        SELECT mesano, DBase, Status 
        FROM TabelaMensal
                                        """ )
        self.consolida.commit()
        table = self.consolidaconecta.fetchall()
	store = self.go('liststore17')
	
	print ' limpa store para não repetir' 
	store.clear()
	
	for row in table:
	    store.append([ row[0], row[1], row[2] ])
	
	
	return (table, store)
    
    
		
    def ListProView1(self, TWList):
	print ' LISTPROVIEW1 ()()()()()() Lista resumo do projeto'  , TWList #= analisar o que pensei quando fiz isso
	
	
	liststore, selection = self.twConsolidar.get_selection().get_selected()
	print ' liststore = ', liststore, ' seleção :   ', selection
	
	
	#selection.connect('changed', self.ListProView()) # sera que funciona????
	
	#model, iter = self.services_treeview.get_selection().get_selected()
	#self.renderer.set_property('editable', True)
	
	#print ' focused?? inicia'
	#col = self.twConsolidar.get_column(1)
	#cell = col.get_cell_renderers()[0]
	#getget = col.cell_get_position(cell)
	#getget = selection.get_state_type()
	#print ' focused?? termina', getget , ' -- ', col
	
	
	
	
	print ' teste de iter ::: ' 
	
	
	
	
	

	
	try:
	    
	    print ' indo testar botão' 
	    self.btnSensitive()		
	    print ' voltando de testar botão'
	    
	    
	    
	    selection = self.twConsolidar.get_selection()
	    selection.set_mode(gtk.SELECTION_SINGLE)
	    tree_model, tree_iter = selection.get_selected()
	    print ' @@@@@@@@@@@@@@@@@@@@@@@' ,  tree_model, tree_iter
	    db_ = tree_model.get_value(tree_iter, 1)
	
	    print db_
	
	    BD = str(db_ + ".db")
	    print BD
	    self.consolidado = sqlite3.connect(BD)
	    self.consolidadoconecta = self.consolidado.cursor()
	
	
	
	
	
	except:
	    print ' deu pau na seleção do liststore'
	    
	    # ver para onde enviar, não adianta mandar para banco em uso
	    pass
	    return
	
	
	
	self.consolidadoconecta.execute("""
            SELECT projeto.pro_nome, projeto.cliente, projeto.valor, SUM (rateiorecurso.valor)
            FROM rateiorecurso, projeto
	    WHERE rateiorecurso.row_pro = projeto.row_pro
            GROUP BY rateiorecurso.row_pro

                                """)
        self.consolida.commit()
	table = self.consolidadoconecta.fetchall()
	store = self.go('liststore18')
	store.clear()
	for row in table:
	    store.append([ row[0], row[1],
	    locale.currency(row[2], grouping=True),
	    locale.currency(row[3], grouping=True) ])
	    print  row[0], row[1], row[2], row[3]
	# locale.currency(row[2], grouping=True)
	
	
	
	
	"""
	    SELECT rateio.row_rec, recursos.nome, SUM (valor_tot)
            FROM rateio, recursos
            WHERE rateio.row_rec = recursos.row_rec
            GROUP BY  rateio.row_rec
	"""
	
	
	
    def AdicionarBD(self, *a):
	
	print 'Adicionar Banco de Dados' # copiado do AdicionaCusto
	
	#---------------- Atenção
	#   tem um unique, então não pode ser repetida.
	#
	#-----------------------------------------------
    
	DBasex = ""
        Statusx = "Vazio"
	
	#try:
	self.consolidaconecta.execute("""
	SELECT DBase
	FROM TabelaMensal 
	WHERE DBase = ? """, (DBasex,))
	
	print 'RESULTADO = =' 
	self.consolida.commit()
	
	table = self.consolidaconecta.fetchall()
	#store = self.go('liststore18')
	store = [ ]
	
	if table: # == []:
	    
	    print 'table cheia'	    
	    self.AdicionarCon.set_sensitive(False)
	    
	    print self.consolidaconecta.rowcount
	    
	    #(number_of_rows,)=self.consolidaconecta.fetchone()
	    #print number_of_rows
	    
	    
	    t1 = 'Já existe um Banco de Dados adicionado'
	    t2 = 'Edite o título do novo Banco de Dados'
	    t3 = 'Adicionar Banco de Dados Novo'
		
	    dialogoAviso(self, t1, t2, t3)
		    
	    #raw_input( 'RESULRADO esperando ......')
	
	    #except self.consolida.Error, e:
    
	    #print "Error %s  ==>:" % e.args[0]
        	
	

	else:
	     
	    DBasex = getText(self)
	    if DBasex == '':
		print 'vazio'
		#raw_input( ' esta vazio == faz o que????')
		pass
		
	    
	    print 'table vazia '
	    
	    self.consolidaconecta.execute("""
		INSERT INTO TabelaMensal( DBase, Status)
		VALUES(?,?)
					    """,( DBasex, Statusx))
	    self.consolida.commit()
	    
	    self.consolidaconecta.execute("""
		SELECT mesano
		FROM TabelaMensal
		WHERE DBase = ? """, (DBasex,))
	    print ' TESTANDO ==== '
	    self.consolida.commit()
	    
	    a = self.consolidaconecta.fetchall()
	    
	    a = a[0]
	    
	    
	    print ' >>>>>>>', a
	    
	    print 'ARQUIVO ==', str(a[0]) +'.db'
	    
	    
	    #self.ListCusto()
	    #self.inicia() #???????
	    #self._BancoEmUso()
	    self.ListBD()
	    
	    DBasexDB = DBasex + ".db"
	    
	    shutil.copy("Branco.db", DBasexDB)
	    print ' ============== feito !!!!'
	    
	    
	    
	print ' testando o incluir Banco de Dados '
	
	
	
	
	
	
    def sel_row_mesano1 (self):
        selection = self.twConsolidar.get_selection()
        selection.set_mode(gtk.SELECTION_SINGLE)
        tree_model, tree_iter = selection.get_selected()
        a = tree_model.get_value(tree_iter,  0 ) #numero arquivo 515, não sei para que vou querer isso
	b = tree_model.get_value(tree_iter,  1 ) #Maio15 - nome do arquivo
	c = tree_model.get_value(tree_iter,  2 ) #Status do arquivo.
	print '()()()()()()()() = ', a, b, c
        return a, b , c
	
	
    '''
    def copiaarquivo1(self, a1): # não estou usando
	
	(a, b, c) = self.sel_row_mesano1()
	
	print a, b, c, ' A1 ===', a1, self
	
	#peguei o arquivo, agora falta colocar um novo nome
	'shutil,copyfile(src, dst) = copiar arquivo'
	
	
	texto = getText(self)
	self.CopiarCon.set_sensitive(False)
	#self.twConsolidar.set_cursor(-1)    #Cursor 0
	#self.twConsolidar.grab_focus()
	self.twConsolidar.selection_remove_all()
	print ' ||||||||||||||||||||||||||||||||||||||||||\\'
	#self.w.set_sensitive(False)
	
	
	print ' message para COPIAR novo banco -----'
	print texto
	
	
	self.consolidaconecta.execute("""
        SELECT mesano, DBase, Status
        FROM TabelaMensal
        ORDER BY mesano
                                """ )
        self.consolida.commit()
        table = self.consolidaconecta.fetchall()
	print 'copiaarquivo1 = table ======>>', table
	print 'OK'
	print table
	store = []
	for row in table:
            store.append([ row[0], row[1], row[2] ])
	    print store
	    try:		
		if row[2] == 'Em Uso':
		    print 'Em Uso =  ',
		    SRC = row[1] + '(Cópia).db'
		    print 'SRC = ',  SRC
		    break
		else:
		    print '*(*(*(*(*(*( Não tem Em Uso'
	    except:
		print '@#@#@#@#@#@# Não tem Em Uso'
	'shutil,copyfile(src, dst) = copiar arquivo'

	    
    '''
    
    def edita_DB_name(self, a2, a3, valor):
        print 'edita_DB_name =>==>>==>>==>>==>>', self,' ====',  a2, '====',  a3, '====',  valor
	
        row_mesano, b , c = self.sel_row_mesano1()
        
	#Atualiza a Tabela de lista de arquivos.
	tb = 'TabelaMensal'
        query = ("UPDATE "+ tb+ " SET  DBase = ? WHERE mesano = ?")
        print query
        self.consolidaconecta.execute(query, ( valor, row_mesano) )
        self.consolida.commit()
	
	#muda nome do arquivo no diretório.
	
	newFile = valor + '.db'
	oldFile = b +'.db'
	print '========>>>>>>   ',  newFile, oldFile
	
	os.rename(oldFile, newFile)
	
	
	BD_ = self._BancoEmUso()
	
        #self.ListCusto()
	#self.ListCusto1()
	#self.ListCusto2()
    
    




#------- FINAL
    def close_window(a, b):
        sys.exit()



if __name__ == "__main__":
    hwg = principal()
    gtk.main()
