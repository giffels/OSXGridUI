#!/usr/bin/env python
#    Installation and configuration of a Grid UI on Mac OS X
#
#    Copyright (C) 2014  Manuel Giffels <giffels@gmail.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
from osxgridui.tools import get_ca_cert_tarball
from osxgridui.tools import get_etc_path
from osxgridui.tools import unpack_tarball

import os

if __name__ == '__main__':
    ###install ca certificates
    etc_path = get_etc_path()
    grid_security_path = os.path.join(etc_path, 'grid-security')
    if not os.path.exists(grid_security_path):
        os.mkdir(grid_security_path)
    unpack_tarball(url=get_ca_cert_tarball(), path=grid_security_path)
