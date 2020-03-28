#!/usr/bin/env python3
'''
   Copyright 2017 Adi Hezral (hezral@gmail.com)

   This file is part of Activ.

    Activ is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Activ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Activ.  If not, see <http://www.gnu.org/licenses/>.
'''
import os
import signal
import gi
from threading import Event, Thread
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, GdkPixbuf, AppIndicator3, Notify

class IndicatorActiv:
    #global variables
    isAboutOpen = False
    
    #Handles about menu choice
    def about_response(self, widget, param):
        if self.isAboutOpen == False:
            self.isAboutOpen = True
            dialog = Gtk.AboutDialog()
            dialog.set_name('Activ Time Keeper')
            dialog.set_version('0.1')
            dialog.set_authors(['Adi Hezral'])
            dialog.set_comments('A simple example of an about dialog.')
            dialog.set_license('Distributed under the MIT license.\nhttp://www.opensource.org/licenses/mit-license.php')
            dialog.run()
            dialog.destroy()
            self.isAboutOpen = False

    def activ_loop(self):
        stopped = Event()
        def loop():
            activated = 0
            while not stopped.wait(60): # the first call is in `interval` secs
                self.indicator.set_label(str(activated) + "m","")
                activated = activated + 1
        Thread(target=loop).start()    
        return stopped.set

    #functions to handle events
    def quit(self, widget):
        self.start_activ()
        Gtk.main_quit()

   #Initialise
    def __init__(self):
        # indicator id
        AppIndicator3_ID = 'indicator-activ'

        #Create AppIndicator3 object
        self.indicator = AppIndicator3.Indicator.new(AppIndicator3_ID, os.path.abspath('data/blank.svg'), AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_label("0m","")

        #Create notify object
        Notify.init(AppIndicator3_ID)
        self.notification = Notify.Notification.new("<b>Joke</b>",'something', None)
        # Use GdkPixbuf to create the proper image type
        notify_icon = GdkPixbuf.Pixbuf.new_from_file("/home/adi/Work/publicapi-tests/abott.png")
        self.notification.set_icon_from_pixbuf(notify_icon)
        self.notification.set_image_from_pixbuf(notify_icon)
        #self.notification.show()
        
        #Create menu object
        self.menu = Gtk.Menu()
        #About
        menuItemAbout = Gtk.MenuItem('About')
        menuItemAbout.connect("activate", self.about_response, "About")
        self.menu.append(menuItemAbout)
        self.menu.append(Gtk.SeparatorMenuItem.new())
        #Quit
        menuItemQuit = Gtk.MenuItem('Quit')
        menuItemQuit.connect('activate', self.quit)
        self.menu.append(menuItemQuit)
        #Show all in menu (instead of calling .show() for each item)
        self.menu.show_all()
        #Add constructed menu as indicator menu
        self.indicator.set_menu(self.menu)
        
        #start loop
        self.start_activ = self.activ_loop()





def main():
    Gtk.main()
    return 0

if __name__ == "__main__":
    indicator = IndicatorActiv()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
