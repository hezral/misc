#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)

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

import os
import gi
import webbrowser
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite
import constants as cn

class Welcome(Gtk.Box):
        
    # Define variable for GTK global theme
    settings = Gtk.Settings.get_default()

    def __init__(self):
        Gtk.Box.__init__(self, False, 0)

        # Create welcome widget
        welcome = Granite.WidgetsWelcome()
        welcome = welcome.new("Welcome", cn.App.application_description)

        # Welcome voices
        welcome.append("object-inverse", "Dark mode", "Switch to the dark side")
        welcome.append("utilities-terminal", "Open Terminal", "Just an example of action")
        welcome.append("help-contents", "Info", "Learn more about this application")
        
        welcome.connect("activated", self.on_welcome_activated)

        self.add(welcome)

    def on_welcome_activated(self, widget, index):
        if index == 0:
            # Use GTK Dark theme
            if self.settings.get_property("gtk-application-prefer-dark-theme") == True:
                self.settings.set_property("gtk-application-prefer-dark-theme", False)
            else:
                self.settings.set_property("gtk-application-prefer-dark-theme", True)
        elif index == 0:
            # Open terminal
            os.system("io.elementary.terminal")
        else:
            # Open webpage
            webbrowser.open_new_tab("https://github.com/mirkobrombin/Rogu")
        print("Index: "+str(index))
