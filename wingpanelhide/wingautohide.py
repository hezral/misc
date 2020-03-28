#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Very simple autohide for wingpanel (elementary OS Loki)
# Author: Yunn Cortes 
# Web: http://entornosgnulinux.com/
#

import time, subprocess, re

APP_NAME    = 'wingautohide'
APP_VERSION = '0.1'

def Get_PositionX():
    sInfo = subprocess.check_output(
        'xdotool getmouselocation --shell',
        shell=True).decode('utf-8')
    return int(re.search(r'X=(\d{1,})', sInfo).groups()[0]) 

def Get_PositionY():
    sInfo = subprocess.check_output(
        'xdotool getmouselocation --shell',
        shell=True).decode('utf-8')
    return int(re.search(r'Y=(\d{1,})', sInfo).groups()[0]) 

def Get_MoveMouseXY(nPosX, nPosY):
    sInfo = subprocess.check_output(
        'xdotool mousemove ' + str(nPosX) + ' ' + str(nPosY),
        shell=True).decode('utf-8')
    return True

def Get_WindowId():
    try:
        sInfo = subprocess.check_output(
            'xdotool getmouselocation --shell',
             shell=True).decode('utf-8')
    except Exception:
        sInfo = ''
        pass  
    return int(re.search(r'WINDOW=(\d{1,})', sInfo).groups()[0]) 

def Get_Properties(nId):
    try:
        sInfo = subprocess.check_output('xprop -id ' + str(nId) + ' WM_CLASS',shell=True).decode('utf-8')
    except Exception:
        sInfo = ''
        pass  
    return sInfo

def IsWingpanel(nId):
    sInfo     = Get_Properties(nId)
    iFound    = sInfo.find('wingpanel')
    return (iFound > 0)


# ===============
# Main
# ===============

bPanelInit = True
while (bPanelInit):

    nPosX      = Get_PositionX()
    nPosY      = Get_PositionY()
    Get_MoveMouseXY(10, 0)
    nIdPanel   = Get_WindowId()
    Get_MoveMouseXY(nPosX, nPosY)

    if (nIdPanel > 0):
        if (not IsWingpanel(nIdPanel)):
	    nIdPanel = 0

    while (nIdPanel > 0):

        bPanelInit = False
        bHideen    = True
	SIZE_PANEL = 4
	SHOW_CMD   = 'xdotool windowmap   ' + str(nIdPanel)
	HIDE_CMD   = 'xdotool windowunmap ' + str(nIdPanel)

	try:
	    subprocess.call(HIDE_CMD, shell=True)

	    while True:

		time.sleep(0.2)
		nPosY       = Get_PositionY()
		nId         = Get_WindowId()
		bPanel      = (nId == nIdPanel)
		bWinPanelON = (nPosY < SIZE_PANEL)

		if (bWinPanelON and bHideen) or (bPanel):
		    subprocess.call(SHOW_CMD, shell=True)
		    bHideen = False
                    iTimesleep = 4
                    while (iTimesleep > 0):

                        time.sleep(0.2)
			nPosY       = Get_PositionY()
			nId         = Get_WindowId()
			bPanel      = (nId == nIdPanel)
			bWinPanelON = (nPosY < SIZE_PANEL)

            		if (bWinPanelON) or (bPanel):
                            iTimesleep = 4

                        iTimesleep = iTimesleep - 0.2

		else:
		    subprocess.call(HIDE_CMD, shell=True)
		    bHideen = True

        finally:
	    subprocess.call(SHOW_CMD, shell=True)

    if (bPanelInit):
        time.sleep(5)