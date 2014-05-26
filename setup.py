#!usr/bin/env python
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

from distutils.core import setup
import glob
import os


def get_data_files(start_dir):
    for dirpath, dirnames, filenames in os.walk(start_dir):
        yield (os.path.join(dirpath, ''),
               [os.path.join(dirpath, filename) for filename in filenames])


setup(name = 'OSXGridUI',
      version = '0.1',
      author = 'Manuel Giffels',
      author_email = 'giffels@gmail.com',
      description = 'Installation and configuration of a Grid UI on Mac OS X',
      url = 'https://github.com/giffels/OSXGridUI',
      data_files = list(get_data_files('etc')) + list(get_data_files('bin')))
