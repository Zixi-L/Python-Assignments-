from Lab2SqlDataBase import co2_sql
import sqlite3

class Get_top_ten:
    def __init__(self):
        self.__getitem__()
        self.sort_dic()
        self.top_ten()
    
    def __getitem__(self):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
    
            sqlite_select_query = """SELECT * from SqliteDb_developers"""  # select all the cols from the database
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            
            self.country_data_dic = {}
            
            for row in records:    
                self.country_data_dic[row[0]] = float(row[4].strip('%'))
        
            cursor.close()        
    
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")            
    
    def sort_dic(self):
        self.sorted_country_data_dic = {k: v for k,v in sorted(self.country_data_dic.items(), key = lambda item: item[1])} # ?????
        self.sorted_country_data_dic.pop('')
        self.sorted_country_data_dic.pop('World')
        self.sorted_country_data_dic.pop('World – International Shipping')
        #print(self.sorted_country_data_dic)
        
    def top_ten(self):
        self.labels = list(self.sorted_country_data_dic.keys())[-10::]
        self.Co2_data = list(self.sorted_country_data_dic.values())[-10::]
        #print(self.Co2_data)

    def get_top_ten_labels(self):
        return self.labels
    
    def get_top_ten_Co2_data(self):
        return self.Co2_data
    
        
    def get_sorted_country_data_dic(self):
        return self.sorted_country_data_dic


test = Get_top_ten()
test.get_sorted_country_data_dic()
    
    