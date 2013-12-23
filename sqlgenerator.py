""" Feed table and columns of the CORE scheme this python script will generate SQL to compare two CORE schemes.
Author : Paul Berden
Date : 2013-12-19

"""

import csv as csv
import numpy as np
import os as os

#Set variables
schema1 = "TAS21_INFA_CORE"
schema2 = "BCO_CORE"

#......Import data and prepare for processing......#

#Read csv file
csv_file_object = csv.reader(open('result.csv', 'rb')) #Load in the csv file
header = csv_file_object.next() #Skip the first line as it is a header
data=[] #Create a variable called 'data'
for row in csv_file_object: #Skip through each row in the csv file
    data.append(row) #adding each row to the data variable

#Create unique table list
tables = []
for row in data:
    tables.append(row[0])
tables = list(set(tables)) #make list distinct
tables.sort() #sort tables ascending


#.......Functions to write the SQL statements.......#

#Function to write the SELECT
def write_select(table, schema):
    print "SELECT "
    for column in data:
        if(table == column[0]):
            print column[1]+", ",
    print "TAS_SOURCE_ID"
    print "FROM "+schema+"."+table

#Function to write SQL statements with MINUS
def write_minus(schema1, schema2):
    for table in tables:
        write_select(table, schema1)
        print "MINUS"
        write_select(table, schema2)
        print ";"

#write_minus(schema1, schema2)


#..Functions to make valid table name for FitNesse..#

#e.g. CORE_DELIVERY_BLOCK >> CoreDeliveryBlock
table = "CORE_DELIVERY_BLOCK"

def valid_fitname(name):
    #all lower case
    locase = name.lower()
    #Make first upper case
    fupper = locase[0].upper()+locase[1:]
    return remove_underscores(fupper)

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

print valid_fitname(table)




#create folder on OS:        os.makedirs(table)
