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

class Sidebar(Gtk.TreeView):
    def __init__(self):
        Gtk.TreeView.__init__(self)

        # configure treeview properties
        self.set_headers_visible(False)
        self.set_enable_tree_lines(False)
        self.set_enable_search(True)
        self.set_size_request(160, -1)

        # Renderer
        self.cell_renderer = Gtk.CellRendererText()   

        # TreeViewColumn
        self.treeview_column = Gtk.TreeViewColumn()

        # TreeStore
        self.tree_store = Gtk.TreeStore(str)

        self.treeview_column.set_title("Local Logs")
        self.treeview_column.pack_start(self.cell_renderer, True)
        self.treeview_column.add_attribute(self.cell_renderer, "text", 0)

        # item
        self.list_item = self.tree_store.append(None, ["SYSTEM"])
        self.tree_store.append(self.list_item, ["system.log"])

        self.list_item = self.tree_store.append(None, ["USER"])
        self.tree_store.append(self.list_item, ["some.log"])

        # add to list
        self.append_column(self.treeview_column)
        self.set_model(self.tree_store)

        # expand all rows
        self.expand_all()

    def on_activated(self, widget, row, col):
        model = widget.get_model()
        text = model[row][0]
        print(text)
