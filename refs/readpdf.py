# -*- coding: utf-8 -*-
# Copyright (C) 2009  Luís Pedro Coelho <lpc@cmu.edu>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

from __future__ import division, with_statement
import hashlib
import pyPdf
import os

def md5sum(filename, nbytes=None, include_size=None):
    '''
    M = md5sum(filename, nbytes=None, include_size=None)

    Similar to running md5sum filename on the commandline.
    '''
    if nbytes is not None and include_size is None:
        include_size = True
    M = hashlib.md5()
    filesize = os.stat(filename).st_size
    if include_size:
        M.update(str(filesize))
    if nbytes is not None:
        filesize = min(filesize, nbytes)
    input = file(filename)
    while filesize > 0:
        s = input.read(32*1024)
        M.update(s)
        filesize -= len(s)
    return M.hexdigest()

def geturi(filename):
    '''
    uri = geturi(filename)
    '''
    md5 = md5sum(filename, 1024**2, include_size=True)
    return 'bib+md5sum:%s?filesize=1MiB' % md5

def gettitle(filename):
    '''
    title = gettitle(filename)

    Returns the /Title attribute from the PDF meta-data or None if it
    doesn't exist
    '''
    if not filename.endswith('.pdf'):
        raise Exception("gettitle: Cannot handle '%s'" % filename)
    P  = pyPdf.PdfFileReader(file(pdffile))
    info = P.getDocumentInfo()
    return info.get('/Title',None)


# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
