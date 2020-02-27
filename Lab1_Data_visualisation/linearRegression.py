import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression
import csv
import lab1_backEnd
from lab1_backEnd import Import_data

class Linear_Regression:
    def __init__(self):
        self.printGraph()
         
    def printGraph(self):
        temp_data = Import_data('Temperature.html' ,"[+-]?\d+(?:\.\d+)?")    
        x_list_str = temp_data.get_year_xaxis_list()
        x_list_int = list([int(s) for s in x_list_str]) # 
        
        y_list_float = temp_data.get_y_axis_list()   
        
        # ---- a reduntant way to get the data for the linear regression calculation
        #with open('xydata.csv', 'w') as f:
            #writer = csv.writer(f)
            #writer.writerows(zip(x_list_int, y_list_float))
            
        #data = pd.read_csv('xydata.csv')  # load data set
        #X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
        #Y = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
        
        
        X = np.array(x_list_int).reshape(-1, 1)
        Y = np.array(y_list_float).reshape(-1, 1)        
        
        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X, Y)  # perform linear regression
        Y_pred = linear_regressor.predict(X)  # make predictions
        plt.scatter(X, Y)
        plt.plot(X, Y_pred, color='red')
        
        axes = plt.gca()  
        axes.set_xlim(x_list_int[0],x_list_int[-1]) 
        axes.set_ylim(temp_data.get_y_axis_min(),temp_data.get_y_axis_max())
        
        plt.xlabel('Years')
        plt.ylabel('Temperature Differential')
        
        
        plt.title('Linear Regression')
        
        plt.show()