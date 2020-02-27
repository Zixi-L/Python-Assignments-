from Lab2ReadHtml import Read_html
import re
import sqlite3

class co2_sql:
    
    def __init__(self):
        pass
    
    def create_table(self):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()    
            cursor.execute("CREATE TABLE IF NOT EXISTS SqliteDb_developers(Country UNIQUE,FCE1990, FCE2005 , FCE2017 , FCE2017_of_world, FCE2017vs1990, Per_Land_Area, Per_Capita)")
            cursor.close()
            
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    #print("The SQLite connection is closed")
                    
            
    def insert_data(self,Country,FCE1990, FCE2005 , FCE2017 , FCE2017_of_world, FCE2017vs1990, Per_Land_Area, Per_Capita):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()
            #print("Successfully Connected to SQLite")
            sqlite_insert_query = """INSERT INTO SqliteDb_developers
                                     (Country,FCE1990, FCE2005 , FCE2017 , FCE2017_of_world, FCE2017vs1990, Per_Land_Area, Per_Capita) 
                                      VALUES 
                                     (?,?,?,?,?,?,?,?)"""
            data_tuple = (Country,FCE1990, FCE2005 , FCE2017 , FCE2017_of_world, FCE2017vs1990, Per_Land_Area, Per_Capita)
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
                print("FCE1990: ", row[1]) 
                print("FCE2005: ", row[2])
                print("FCE2017: ", row[3])
                print("FCE2017_of_world:",row[4])
                print("FCE2017vs1990:",row[5])
                print("Per_Land_Area:",row[6])
                print("Per_Capita:",row[7])
                print("\n")
    
            cursor.close()
    
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")
                
                
def main():
    sql_obj=co2_sql()
    sql_obj.create_table()
    
    read_obj = Read_html("https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions")
    read_obj.get_table()
    
    for l in read_obj.get_table():
        sql_obj.insert_data(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7])    

    #sql_obj.readSqliteTable()
    
main()