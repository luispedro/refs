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
import sqlite3

_connection = None
def lazy_connect():
    global _connection
    if _connection is None:
        _connection = sqlite3.connect('refs.db')
    return _connection.cursor()
    
def lookup(url):
    '''
    bib = lookup(url)

    Return None if not in database.
    '''
    cursor = lazy_connect()
    res = cursor.execute('''
        SELECT bid
        FROM links
        WHERE url = ?''',
        url)
    res = res.fetchall()
    if not res:
        return None
    return res[0][0]

def add(bibliography, url=None):
    '''
    add(bibliography, url=None)

    '''
    cursor = lazy_connect()
    if bibliography.id is not None:
        cursor.execute('''
            INSERT INTO bibs(bid,author,title) VALUES(?,?,?)''',
            bibliography.id, bibliography.author, bibliography.title)
    else:
        cursor.execute('''
            INSERT INTO bibs(author,title) VALUES(?,?)''',
            bibliography.author, bibliography.title)
        cursor.execute('''
            SELECT MAX(bibs.bid)
            FROM bibs''')
        bibliography.id = cursor.fetchone()[0]


def addlink(bibliography, url):
    '''
    addlink(bibliography, url)
    '''
    if lookup(url) is not None:
        raise Exception('refs.DB.addlink: url is already linked!')
    if bibliography.id is None:
        raise Exception('refs.DB.addlink: bid is None!')
    cursor = lazy_connect()
    cursor.execute('''
        INSERT INTO links
        VALUES(?,?)''', bibliography.id, url)

def update(bibliography):
    '''
    update(bibliography)
    '''
    if bibliography.id is None:
        raise Exception('DB.update: cannot update bibliography without a bibid')

    cursor = lazy_connect()
    cursor.execute('''
        UPDATE bibs
        SET title = ?,
            author = ?,
            date_published = ?
        WHERE bid = ?
        ''', bibliography.title, bibliography.author, bibliography.date_published, bibliography.id)

# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
