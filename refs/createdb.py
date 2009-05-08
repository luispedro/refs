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
from os.path import dirname
from . import DB

def createdb():
    cursor = DB.lazy_connect()
    input = [line for line in file(dirname(__file__)+'/schema.sql') if not line.startswith('--')]
    input = '\n'.join(input)
    for s in input.split(';'):
        s = s.strip()
        if not s: continue
        cursor.execute(s)

# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
