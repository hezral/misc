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
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Granite
import constants as cn
import welcome as wl

class Tabs(Granite.WidgetsDynamicNotebook):
    def __init__(self):
        Granite.WidgetsDynamicNotebook.__init__(self)
        #setup notebook properties
        self.show_tabs = true
        self.allow_restoring = true
        self.allow_duplication = true
        self.allow_new_window = false
        self.group_name = cn.App.application_name
        
        #workaround for no icon on tabs
        self.tab_icon = Gio.FileIcon.new(Gio.File.new_for_path('data/blank.svg'))
        
        #startup setup for first run
        on_startup()

        #connect signals
        self.connect('tab_removed',on_tabs_removed)
        
        self.show()
    
    def on_startup(self):
        self.welcome = wl.Welcome()
        self.tab_welcome = Granite.WidgetsTab.new("Welcome", self.tab_icon, self.welcome)
        self.insert_tab(tab_welcome, 0)
        self.current = tab_welcome

    def on_tabs_removed(self):
        if self.get_n_tabs() == 0:
            on_startup

