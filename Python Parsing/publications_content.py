#!/usr/bin/env python
# coding=utf-8

__author__ = 'Alexandre Connat'

######################################################################################
### Parse the publications_content.csv file, and import data to the MySQL database ###
######################################################################################

import Database as DB
import Parse as Parse
import csv

# Parse data from csv file

filename = 'Books/publications_content.csv'
f = open(filename, 'rU')
f.seek(0)

fields = ['id', 'title_id', 'publication_id']
reader = csv.DictReader(f, dialect='excel-tab', fieldnames=fields)

data = []
for row in reader:
    data.append( (row['id'], row['title_id'], row['publication_id']) )


# Insert data into Database

# db = DB.Database('db4free.net','group8','toto123', 'cs322')
#
# sql = 'INSERT INTO Title_is_part_of_Publication (title_id, publication_id) VALUES (%s, %s);'
# db.insertMany(sql, data)