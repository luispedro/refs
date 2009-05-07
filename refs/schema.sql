-- Copyright (C) 2009  Luis Pedro Coelho <lpc@cmu.edu>
--
-- This program is free software; you can redistribute it and/or modify
-- it under the terms of the GNU General Public License as published
-- by the Free Software Foundation; either version 2 of the License,
-- or (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful, but
-- WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
-- General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program; if not, write to the Free Software
-- Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
-- 02110-1301, USA.

CREATE TABLE bibs (
    bid INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    date_published VARCHAR(255));

CREATE TABLE bib_extra_fields (
    bfid INT PRIMARY KEY,
    name VARCHAR(255));

CREATE TABLE bib_extra (
    bid INT NOT NULL,
    bfid INT NOT NULL,
    value VARCHAR(255));

CREATE TABLE links (
    uri VARCHAR(255) PRIMARY KEY,
    bid INT NOT NULL);

CREATE INDEX ids_uri_idx ON links(uri);

