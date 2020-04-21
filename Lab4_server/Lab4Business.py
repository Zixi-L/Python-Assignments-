import sqlite3
import re
import xml.etree.ElementTree as ET

'''
This file creates the sqlite table, and do not interact with other files. 
'''

class UN_data:
    def __init__(self):
        self.create_table()
        

    def create_table(self):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()    
            cursor.execute("CREATE TABLE IF NOT EXISTS SqliteDb_developers(Country, Year, Value)")
            cursor.close()
            
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    #print("The SQLite connection is closed")
                    
    def insert_data(self,Country, Year, Value):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()
            #print("Successfully Connected to SQLite")
            sqlite_insert_query = """INSERT INTO SqliteDb_developers
                                     (Country, Year, Value) 
                                      VALUES 
                                     (?,?,?)"""
            data_tuple = (Country, Year, Value)
            cursor.execute(sqlite_insert_query, data_tuple)
            sqliteConnection.commit()
            #print("Record inserted successfully into SqliteDb_developers table ")
            cursor.close()
            
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    #print("The SQLite connection is closed")
                    
    def readSqliteTable(self):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
    
            sqlite_select_query = """SELECT * from SqliteDb_developers"""  # select all the cols from the database
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print("Total rows are:  ", len(records))
            print("Printing each row")
            for row in records:
                print("Country: ", row[0])
                print("Year: ", row[1]) 
                print("Value: ", row[2])
                print("\n")
    
            cursor.close()
    
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")
                
        


def main():
    UN_data_obj = UN_data()
    tree = ET.parse('UNdata.xml')            
    root = tree.getroot()
    
    country = []
    year = []
    value = [] 

    for child in root:
        for record in child:
            country = record.findall('Country')
            year = record.findall('Year')
            value = record.findall('Value') 
            UN_data_obj.insert_data(country[0].text, year[0].text,value[0].text)

            
    
    UN_data_obj.readSqliteTable()

    
    #print(len(self.country),len(self.year),len(self.value))  = 1204
   
    
main()