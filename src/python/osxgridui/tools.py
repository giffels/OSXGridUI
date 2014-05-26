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
from optparse import OptionParser

import re
import sys
import tarfile
import urllib2

def cmd(cmd):
    try:
        retcode = subprocess.call(cmd, shell=True)
    except OSError as error:
        print >> sys.stderr, "An error has occurred:", error
    else:
        if  retcode < 0:
            print >> sys.stderr, "The subprocess was terminated by SIGNAL %s" % -retcode
        return retcode


def create_url_object(url):
    return urllib2.urlopen(url)


def get_ca_cert_tarball():
    url_object = create_url_object("http://software.grid.iu.edu/pacman/cadist/ca-certs-version")
    tarball_pattern = r"^tarball=(?P<url>\S+).*"
    tarball_regex = re.compile(tarball_pattern)
    for line in url_object:
        match_obj = tarball_regex.match(line)
        if match_obj:
            return match_obj.groupdict()['url']
    return None


def get_etc_path():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-e", "--etc-path", dest="etc_path",
                      help="etc path on your system", metavar="ETCPATH")

    (options, args) = parser.parse_args()

    if not options.etc_path:
        parser.print_usage()
        parser.error("options --etc-path is mandatory")

    return options.etc_path


def unpack_tarball(url, path, mode='r|gz'):
    url_object = create_url_object(url)
    with tarfile.open(fileobj=url_object, mode=mode) as f:
        f.extractall(path=path)
