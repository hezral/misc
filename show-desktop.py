#!/usr/bin/env python3
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

def get_winlist(scr=None, selecttype=None):
    """
    get the window list. possible args: screen, select_type, in case it is
    already fetched elsewhere. select type is optional, to fetch only
    specific window types.
    """
    if not scr:
        scr = Wnck.Screen.get_default()
        scr.force_update()
    windows = scr.get_windows()
    if selecttype:
        windows = [w for w in windows if check_windowtype(w, selecttype)]
    return windows

wlist = get_winlist()
for w in wlist:
    print(w.get_name(), ",", w.is_maximized())

screen = Wnck.Screen.get_default()
screen.toggle_showing_desktop(True)
