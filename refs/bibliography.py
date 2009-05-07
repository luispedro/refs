# -*- coding: utf-8 -*-
# Copyright (C) 2009 Luís Pedro Coelho <lpc@cmu.edu>
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

_allowed_bibtypes = ['article','inproceedings']

class Bibliography(object):
    '''
    Represents a bibliography.
    '''
    def __init__(self, **kwargs):
        self.id = kwargs.get('id',None)
        self.author = kwargs.get('author',None)
        self.title = kwargs.get('title',None)
        self.bibtype = kwargs.get('bibtype',None)
        if self.bibtype is not None and self.bibtype not in _allowed_bibtypes:
            raise Exception("Bibliography: unknown bibtype '%s'" % self.bibtype)

# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
