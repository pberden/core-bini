""" Feed table and columns of the CORE scheme this python script will generate SQL to compare two CORE schemes.
Author : Paul Berden
Date : 2013-12-19

"""

import csv as csv
import numpy as np

#Set variables
schema1 = "TAS21_INFA_CORE"
schema2 = "BCO_CORE"

#Read csv file
csv_file_object = csv.reader(open('result.csv', 'rb')) #Load in the csv file
header = csv_file_object.next() #Skip the fist line as it is a header
data=[] #Creat a variable called 'data'
for row in csv_file_object: #Skip through each row in the csv file
    data.append(row) #adding each row to the data variable

#data = np.array(data) #Then convert from a list to an array

#Create unique table list
tables = []
for row in data:
    tables.append(row[0])
tables = list(set(tables)) #make list distinct
tables.sort()

#Function to write the SELECT
def write_select(table, schema):
    print "SELECT "
    for column in data:
        if(table == column[0]):
            print column[1]+", ",
    print "TAS_SOURCE_ID"
    print "FROM "+schema+"."+table

def write_minus(schema1, schema2):
    for table in tables:
        write_select(table, schema1)
        print "MINUS"
        write_select(table, schema2)
        print ";"

write_minus(schema1, schema2)
