from Lab3Agents import Agents
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt 
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import sqlite3

class Linear_Regression:
    def __init__(self):
        self.__getitem__()

    def __getitem__(self):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
    
            sqlite_select_query = """SELECT * from SqliteDb_developers"""  # select all the cols from the database
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            
            self.x_year = []
            self.y_axis = []
            
            self.graph_id = int(input('Please entre 1-6 to choose a graph(1 CO2; 2 CH4; 3 N2O; 4 CFC12; 5 CFC11; 6 _15_minor_list): '))            
            
            for row in records:    
                self.x_year.append(float(row[0]))
                self.y_axis.append(float(row[self.graph_id]))
                
            cursor.close()        
    
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")            
                       
        X = np.array(self.x_year).reshape(-1, 1)
        Y = np.array(self.y_axis).reshape(-1, 1)        
        
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X, Y)  # perform linear regression
        Y_pred = linear_regressor.predict(X)  # make predictions
        plt.scatter(X, Y)
        plt.plot(X, Y_pred, color='red')
        
        axes = plt.gca()  
        axes.set_xlim(self.x_year[0],self.x_year[-1]) 
        #axes.set_ylim(temp_data.get_y_axis_min(),temp_data.get_y_axis_max())
        
        plt.xlabel('Years')
        plt.ylabel('CO2-equivalent')
        
        plt.title('Linear Regression')
        
        plt.show()


test = Linear_Regression()
    
