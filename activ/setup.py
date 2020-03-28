#!/usr/bin/python3

import glob, os
from distutils.core import setup

install_data = [('share/metainfo', ['data/com.github.hezral.indicator-activ.appdata.xml']),
                ('share/applications', ['data/com.github.hezral.indicator-activ.desktop']),
                ('share/icons/hicolor/128x128/apps',['data/com.github.hezral.indicator-activ.svg']),
                ('bin/activ',['data/style.css']),
                ('bin/activ',['activ/alert.py']),
                ('bin/activ',['activ/constants.py']),
                ('bin/activ',['activ/create.py']),
                ('bin/activ',['activ/detail.py']),
                ('bin/activ',['activ/headerbar.py']),
                ('bin/activ',['activ/helper.py']),
                ('bin/activ',['activ/list.py']),
                ('bin/activ',['activ/main.py']),
                ('bin/activ',['activ/stack.py']),
                ('bin/activ',['activ/welcome.py']),
                ('bin/activ',['activ/window.py']),
                ('bin/activ',['activ/wine.py']),
                ('bin/activ',['activ/__init__.py']),
                ('bin/activ/locale/it_IT/LC_MESSAGES',['activ/locale/it_IT/LC_MESSAGES/activ.mo']),
                ('bin/activ/locale/it_IT/LC_MESSAGES',['activ/locale/it_IT/LC_MESSAGES/activ.po'])]

setup(  name='activ',
        version='0.1',
        author='Adi Hezral',
        description='Easily check how long you've been using your computer'',
        url='https://github.com/hezral/activ',
        license='GNU GPL3',
        scripts=['com.github.hezral.indicator-activ'],
        packages=['activ'],
        data_files=install_data)
