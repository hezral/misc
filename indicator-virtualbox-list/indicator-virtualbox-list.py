#!/usr/bin/env python3

import os
import signal
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

have_appindicator = True
try:
    gi.require_version('AppIndicator3', '0.1')
    from gi.repository import AppIndicator3 as appindicator
except:
    have_appindicator = False

have_notify = True
try:
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify
except:
    have_Notify = False

class OracleVMToolboxIndicator:

    #global variables
    isAboutOpen = False

    #functions to handle events
    def quit(self, widget, data=None):
        Notify.uninit()
        Gtk.main_quit()

    #Handles about menu choice
    def about_response(self, w, param):
        if self.isAboutOpen == False:
            self.isAboutOpen = True
            #Show about window
            #actually show a constructed window
            #MAKE CERTAIN that the isAboutOpen property is set to False when the window is destroyed!
            #print(param)
            Notify.Notification.new("<b>About</b>", 'indicator-oracle-vm-toolbox by <b>Adi</b>', None).show()
            self.isAboutOpen = False

   #Initialise
    def __init__(self):
        # indicator id
        APPINDICATOR_ID = 'indicator-oracle-vm-toolbox'

        #Create appindicator object
        if have_appindicator:
            self.indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('icon-virtualbox-list-off.svg'),
                                                  appindicator.IndicatorCategory.SYSTEM_SERVICES)
            self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        else:
            self.indicator = Gtk.status_icon_new_from_stock(Gtk.STOCK_HOME)

        #Create menu object
        self.menu = Gtk.Menu()

        #Add menu items below

        #Virtual Machine list sub menu
        menuItemVMs = Gtk.MenuItem('Virtual Machines')
        menuItemVMs.connect("activate",self.about_response,"VMs")
        self.menu.append(menuItemVMs)
        self.menu.append(Gtk.SeparatorMenuItem.new())

        #switch


        #About
        menuItemAbout = Gtk.MenuItem('About')
        menuItemAbout.connect("activate", self.about_response, "About")
        self.menu.append(menuItemAbout)
        self.menu.append(Gtk.SeparatorMenuItem.new())

        #submenu
        imenu = Gtk.Menu()

        importm = Gtk.MenuItem("Import")
        importm.set_submenu(imenu)

        inews = Gtk.MenuItem("Import news feed...")
        ibookmarks = Gtk.MenuItem("Import bookmarks...")
        imail = Gtk.MenuItem("Import mail...")

        imenu.append(inews)
        imenu.append(ibookmarks)
        imenu.append(imail)

        self.menu.append(importm)

        self.menu.append(Gtk.SeparatorMenuItem.new())

        #Quit
        menuItemQuit = Gtk.MenuItem('Quit')
        menuItemQuit.connect('activate', self.quit)
        self.menu.append(menuItemQuit)

        #Show all in menu (instead of calling .show() for each item)
        self.menu.show_all()

        #Add constructed menu as indicator menu
        self.indicator.set_menu(self.menu)

        #Initialize Notify
        Notify.init(APPINDICATOR_ID)
        Notify.Notification.new("<b>Joke</b>",'something', None).show()

def main():
    Gtk.main()
    return 0

if __name__ == "__main__":
    indicator = OracleVMToolboxIndicator()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
