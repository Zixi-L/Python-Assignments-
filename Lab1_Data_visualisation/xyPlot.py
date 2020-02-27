import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import lab1_backEnd
from lab1_backEnd import Import_data

class Xy_plot_graph:
    def __init__(self):
        self.print_xygraph()
        
    def print_xygraph(self):
        
        temp_data = Import_data('Temperature.html' ,"[+-]?\d+(?:\.\d+)?")    
        x_list_str = temp_data.get_year_xaxis_list()
        x_list_int = [int(s) for s in x_list_str]  
        
        y_list_float = temp_data.get_y_axis_list()   
        
        axes = plt.gca()   # gca(): get the current axis
        axes.set_xlim(x_list_int[0],x_list_int[-1])  # set the range of x lim 
            
        axes.set_ylim(temp_data.get_y_axis_min(),temp_data.get_y_axis_max()) # set the range of y lim
        
        
        
        
        plt.xlabel('Years')
        plt.ylabel('Temperature Differential')
        plt.title('XY Plot')
            
        plt.plot(x_list_int,y_list_float) # get the plots
        plt.show()    
    
