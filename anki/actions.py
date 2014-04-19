#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def install():
	
    pisitools.dobin("runanki", "/usr/bin/")
    pisitools.insinto("/usr/share/anki/", "anki")
    pisitools.insinto("/usr/share/anki/", "aqt")
    pisitools.insinto("/usr/share/pixmaps/", "anki.png")
    pisitools.insinto("/usr/share/pixmaps/", "anki.xpm")
    pisitools.insinto("/usr/share/applications/", "anki.desktop")
    pisitools.insinto("/usr/share/anki/", "thirdparty/send2trash")
    pisitools.dodoc("README", "LICENSE")
