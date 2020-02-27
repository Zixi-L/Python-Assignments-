import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd
from pandas import Series, DataFrame
import lab1_backEnd
from lab1_backEnd import Import_data

class Bar_chart_graph:
    def __init__(self):
        self.pring_barChart_graph()


    def pring_barChart_graph(self):
        
        temp_data = Import_data('Temperature.html' ,"[+-]?\d+(?:\.\d+)?")    
        
        x_list_str = temp_data.get_year_xaxis_list()
        x_list_int = [int(s) for s in x_list_str]    
        
        y_list_float = temp_data.get_y_axis_list() 
        
        plt.bar(x_list_int,y_list_float)
        
        axes = plt.gca()
        axes.set_xlim(x_list_int[0],x_list_int[-1])
        axes.set_ylim(temp_data.get_y_axis_min(),temp_data.get_y_axis_max())    
        
        plt.xlabel('Years')
        plt.ylabel('Temperature Differential')   
        plt.title('Bar Chart')
        
        plt.show()