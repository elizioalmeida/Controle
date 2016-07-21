#!/usr/bin/env python
# coding:utf-8
# -*- coding: utf_8 -*-


#------ CONSOLIDADO

def ListProjCons(self, *a): #liststore17
    
    #eliminado
    pass
    
	    
def ListProView( self): #, TWList):
    print ' Lista resumo do projeto' #, TWList
    selection = self.twConsolidar.get_selection()
    selection.set_mode(gtk.SELECTION_SINGLE)
    tree_model, tree_iter = selection.get_selected()
    print ' @@@@@@@@@@@@@@@@@@@@@@@' ,  tree_model, tree_iter
    db_ = tree_model.get_value(tree_iter, 1)
    
    print db_
    
    BD = str(db_ + ".db")
    self.consolidado = sqlite3.connect(BD)
    self.consolidadoconecta = self.consolidado.cursor()
    
    
    
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
    
    
    
    
    '''
	SELECT rateio.row_rec, recursos.nome, SUM (valor_tot)
	FROM rateio, recursos
	WHERE rateio.row_rec = recursos.row_rec
	GROUP BY  rateio.row_rec
    '''
def sel_row_mesano (self):
    selection = self.twConsolidar.get_selection()
    selection.set_mode(gtk.SELECTION_SINGLE)
    tree_model, tree_iter = selection.get_selected()
    a = tree_model.get_value(tree_iter,  0 )
    print '()()()()()()()() = ', a
    return a
    
def copiaarquivo(a, selfm): # posso copiar do copiaarquivo1 que esta no main.
    print ' Copia arquivo - Consolidado = HHHHHHHHHHHHHHHHHHHHHHHHHHHHH' , a # a é o botão.
    
    #self = a.parent.parent.parent.parent.parent = não deu muito certo.
        
    print 'selfm: ', selfm
    
    
    
    print '}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}', selfm  #self
        
    selfm.consolidaconecta.execute("""
    SELECT mesano, DBase, Status
    FROM TabelaMensal
    ORDER BY mesano
			    """ )
    selfm.consolida.commit()
    table = selfm.consolidaconecta.fetchall()
    print ' table ======>>', table
    print 'OK'
    print table
    store = []
    for row in table:
	store.append([ row[0], row[1], row[2] ])
	print store
	try:		
	    if row[2] == 'Em Uso':
		print 'Em Uso 2 =  ',
		SRC = row[1] + 'atualizar.db'
		print 'SRC = ',  SRC
		break
	    else:
		print '*(*(*(*(*(*( Não tem Em Uso 2'
	except:
	    print '@#@#@#@#@#@# Não tem Em Uso 2'
    
    
    
    

def edita_status( a2, a3, valor, self):
    print 'EDITA_STATUS1 ()()()()()()()*** = ', a2, a3, valor
    
    row_mesano, b , c = self.sel_row_mesano1()
    print ' Valor( iter) : = ',  c, '    valor da interrupção:   ' ,valor
    
    if valor != c:
	self.consolidaconecta.execute("""
	UPDATE TabelaMensal SET  status = ? WHERE mesano = ?
	    """, ( valor, row_mesano) )
			    
	self.consolida.commit()
	print ' to aqui' 
	#self.ListProjCons1()
	print ' Estou carregando o status vou chamar _BancoEmUso'
    
	BD_ = self._BancoEmUso()
    
	print ' editando status :   ', BD_ , ' vendo se esta vazio ou não agora'
    
    #self.inicia(BD_)
    
    
    #self.inicia()
    else:
	print 'Não mudar nada   000000000000000000000000000000000000000000000'
	#raw_input( ' nao mudar nada ' )
	
	pass

    ''' - Usar se for necessário ver o arquivo que foi modificado por ultimo.
    DBx = '/home/elizio/Dropbox/Projeto/controle/' + row[1] + '.db' 
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime( DBx ))
	
    print mtime
    '''


