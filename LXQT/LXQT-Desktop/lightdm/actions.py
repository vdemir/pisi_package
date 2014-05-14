#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get


def setup():
    autotools.configure("--prefix=/usr  --enable-liblightdm-gobject --disable-gtk-doc \
                         --disable-tests --enable-liblightdm-qt --with-greeter-session=lxqt-lightdm-greeter")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
