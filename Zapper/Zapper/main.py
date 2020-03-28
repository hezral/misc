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
from gi.repository import Gtk, Gdk, Granite
import window as wn

class Application(Granite.Application):

    def do_activate(self):
        win = wn.Window()
        win.set_size_request(640, 480)
        win.set_resizable(True)
        win.set_position(Gtk.WindowPosition.CENTER)
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        Gtk.main()

app = Application()

app.run("", 1)
