""" Feed table and columns of the CORE scheme this python script
will generate the SQL to compare two CORE schemes in DbFit
Author : Paul Berden
Website : www.paulberden.nl
Date : 2014-01-06

"""

import csv as csv
import numpy as np
import os as os

#Set variables
schema1 = "TAS21B03_CORE"
schema2 = "TAS21I03_CORE"

#......Import data and prepare for processing......#

#Read csv file
csv_file_object = csv.reader(open('GetTables/tables.csv', 'rb')) #Load in the csv file
header = csv_file_object.next() #Skip the first line as it is a header
columns=[] #Create a variable called 'data'
for row in csv_file_object: #Skip through each row in the csv file
    columns.append(row) #adding each row to the data variable

#Create unique table list
tables = []
for row in columns:
    tables.append(row[0])
tables = list(set(tables)) #make list distinct
tables.sort() #sort tables ascending


#.......Functions to write the SQL statements.......#

#Function to write the SELECT
def write_select(table, schema):
    print "SELECT "
    for column in columns:
        if(table == column[0]):
            print column[1]+", ",
    print "TAS_SOURCE_ID"
    print "FROM "+schema+"."+table

#Function to write SQL statements with MINUS
def write_minus(table, schema1, schema2):
    print "SELECT COUNT(*) FROM ("
    write_select(table, schema1)
    print "MINUS"
    write_select(table, schema2)
    print ") Q"
    print ";"
    print ""

#..Functions to make valid table name for FitNesse..#

#e.g. CORE_DELIVERY_BLOCK >> CoreDeliveryBlock
#table = "CORE_DELIVERY_BLOCK"

def valid_fitname(name):
    #all lower case
    locase = name.lower()
    #Make first upper case
    fupper = locase[0].upper()+locase[1:]
    return remove_underscores(fupper)

#Recursive function to remove the underscores and make the first letter of eacht word Capital
def remove_underscores(name):
    pos = name.find("_")
    if(pos <> -1):
        #remove underscore
        newstr = name[:pos] + name[pos+1:]
        #make first letter upper case
        upcase = newstr[:pos] + newstr[pos].upper() + newstr[pos+1:]
        return remove_underscores(upcase)
    else:
        return name


#....................Program flow...................#
def run_program():
    for table in tables:
        fitname = valid_fitname(table)
        pathname = "./Write/"+fitname
        os.makedirs(pathname) #create folder on OS
        content = open("./Write/"+fitname+"/content.txt", "w")
#        content.write("TEST")
        content.write(write_minus(table, schema1, schema2))
        content.close()

run_program()
