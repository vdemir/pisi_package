#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():

    shelltools.cd("%s/gendesk-0.6.1/" % get.workDIR()) 
    shelltools.system("go build")
    
    
def install():	
    pisitools.dobin("gendesk-0.6.1", "/usr/bin/")
    shelltools.chmod("%s/gendesk-0.6.1/gendesk-0.6.1" % get.workDIR())
