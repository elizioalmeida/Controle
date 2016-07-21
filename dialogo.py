#!/usr/bin/env python

import gtk
 

def responseToDialog(entry, dialog, response):
    dialog.response(response)
def getText(self):
    
    self.w.set_sensitive(False)
    
    #base this on a message dialog
    dialog = gtk.MessageDialog(
        None,
        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
        gtk.MESSAGE_QUESTION,
        gtk.BUTTONS_OK,
        None)
    dialog.set_markup('Please enter your <b>name</b>:')
    #create the text input field
    entry = gtk.Entry()
    #allow the user to press enter to do ok
    entry.connect("activate", responseToDialog, dialog, gtk.RESPONSE_OK)
    #create a horizontal box to pack the entry and a label
    hbox = gtk.HBox()
    hbox.pack_start(gtk.Label("Name:"), False, 5, 5)
    hbox.pack_end(entry)
    #some secondary text
    dialog.format_secondary_markup("This will be used for <i>identification</i> purposes")
    #add it and show it
    dialog.vbox.pack_end(hbox, True, True, 0)
    dialog.show_all()
    #go go go
    dialog.run()
    text = entry.get_text()
    dialog.destroy()
    self.w.set_sensitive(True)
    return text
    
def dialogoAviso(selfm, t1, t2, t3):

    print t1, t2, t3


    parent = None
    md = gtk.MessageDialog(parent,
	    gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_WARNING,
	    gtk.BUTTONS_OK_CANCEL, t1 )
    md.format_secondary_text(t2)
    md.set_title(t3)
	
    response = md.run()
	
    if response == gtk.RESPONSE_OK:
	md.destroy()
	    
	print '333333333333333333333333333333333333 == voltei? '
	return 1
    elif response == gtk.RESPONSE_CANCEL:
	md.destroy()
	return 2
	    
    
    
    
    
if __name__ == '__main__':
    print "The name was %s" % getText()
    gtk.main()
