#!/usr/bin/python3
'''
   Copyright 2017 Adi Hezral (hezral@gmail.com)

   This file is part of Rogu.

    Rogu is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Rogu is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Rogu.  If not, see <http://www.gnu.org/licenses/>.
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SearchList(Gtk.EntryCompletion):

    def __init__(self):

        Gtk.EntryCompletion.__init__(self)

        def on_match_selected(self, treemodel, treeiter):
            print(treemodel[treeiter][self.get_text_column()])

        self.urls = [ 
            'http://www.google.com',
            'http://www.google.com/android',
            'http://www.greatstuff.com',
            'http://www.facebook.com',
            ]   
        self.liststore = Gtk.ListStore(str)
        for s in self.urls:
            self.liststore.append([s])

        self.set_model(self.liststore)
        self.set_text_column(0)
        self.connect('match-selected', on_match_selected)

