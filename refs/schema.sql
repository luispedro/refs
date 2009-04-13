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
    url VARCHAR(255) PRIMARY KEY,
    bid INT NOT NULL);

CREATE INDEX ids_url_idx ON links(url);

