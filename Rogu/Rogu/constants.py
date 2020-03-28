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

class App:
    application_id = "com.github.hezral.Rogu"
    application_name = "Rogu"
    application_description = "Rogu the Log file viewer"
    application_version ="1.0"
    main_url = "https://github.com/hezral/Rogu"
    bug_url = "https://github.com/hezral/Rogu/issues/labels/bug"
    help_url = "https://github.com/hezral/Rogu/issues"
    about_authors = {"Adi Hezral <hezral@gmail.com>"}
    about_comments = application_description
    about_license_type = Gtk.License.GPL_3_0

class Colors:
    primary_color = "#645552"
    primary_text_color = "#EEEDEC"
    primary_text_shadow_color = "#53433F"
