""" Feed table and columns of the CORE scheme this python script will generate SQL to compare two CORE schemes.
Author : Paul Berden
Date : 2013-12-19

"""

import csv as csv
import numpy as np

#Set variables
schema1 = "TAS_21_BODS_CORE"
schema2 = "TAS_21_BODS_CORE"

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

#Function to loop through the data
def write_sql(schema):
    for table in tables:
        print "SELECT "
        for column in data:
            if(table == column[0]):
                #think of a way to preven a comma after last column!!!
                #do something with length and filter on list??
                print column[1]+", ",
        print "FROM "+schema+"."+table
        print ""

write_sql(schema1)

