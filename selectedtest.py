#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite


class MyApp (object):
    def __init__(self):
        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", gtk.main_quit )
        self.entry = gtk.Entry()
        self.window.selection_convert("PRIMARY", "STRING")
        self.window.connect("selection_received", self.selection_received)
        self.window.add(self.entry)
        self.window.show_all()
    # Signal handler called when the selections owner returns the data
    def selection_received(self, widget, selection_data, data):
        print 'selection_data.type=%r'%selection_data.type
        # Make sure we got the data in the expected form
        if str(selection_data.type) == "STRING":
            self.entry.set_text("Selected Text is : %s"  % selection_data.get_text())

        elif str(selection_data.type) == "ATOM":
            # Print out the target list we received
            targets = selection_data.get_targets()
            for target in targets:
                name = str(target)
                if name != None:
                    self.entry.set_text("%s" % name)
                else:
                    self.entry.set_text("(bad target)")
        else:
            self.entry.set_text("Selection was not returned as \"STRING\" or \"ATOM\"!")

        return False
    def main(self):
        gtk.main()

app=MyApp()
app.main()