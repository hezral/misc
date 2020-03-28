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
from datetime import datetime
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
#Components
import headerbar as hb
import welcome as wl

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Messages")

        self.hbar = hb.Headerbar()
        self.set_titlebar(self.hbar)

        self.welcome = wl.Welcome()

        
        self.add(self.welcome)


