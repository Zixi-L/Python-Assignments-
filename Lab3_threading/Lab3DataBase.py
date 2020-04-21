from Lab3Webscraper import Read_html
import re
import sqlite3

class grf_sql:
    
    def __init__(self):
        pass
    
    def create_table(self):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()    
            cursor.execute("CREATE TABLE IF NOT EXISTS SqliteDb_developers(Year UNIQUE, CO2, CH4 , N2O , CFC12, CFC11, _15minor)")
            cursor.close()
            
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    #print("The SQLite connection is closed")
                    
            
    def insert_data(self,Year, CO2, CH4 , N2O , CFC12, CFC11, _15minor):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()
            #print("Successfully Connected to SQLite")
            sqlite_insert_query = """INSERT INTO SqliteDb_developers
                                     (Year, CO2, CH4 , N2O , CFC12, CFC11, _15minor) 
                                      VALUES 
                                     (?,?,?,?,?,?,?)"""
            data_tuple = (Year, CO2, CH4 , N2O , CFC12, CFC11, _15minor)
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
                print("Year:", row[0])
                print("CO2: ", row[1]) 
                print("CH4: ", row[2])
                print("N2O: ", row[3])
                print("CFC12:",row[4])
                print("CFC11:",row[5])
                print("_15minor:",row[6])
                print("\n")
    
            cursor.close()
    
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")
                
                
def main():
    sql_obj=grf_sql()
    sql_obj.create_table()
    
    read_obj = Read_html("https://www.esrl.noaa.gov/gmd/aggi/aggi.html")
    read_obj.get_table()
    
    for l in read_obj.get_table():
        sql_obj.insert_data(l[0],l[1],l[2],l[3],l[4],l[5],l[6])    

    sql_obj.readSqliteTable()
    
main()