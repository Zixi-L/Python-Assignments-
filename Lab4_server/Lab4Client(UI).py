import sqlite3
from tkinter import*
import socket
import json

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

class GUI:
    def __init__(self):
        self.startClient()
        self.get_country_name()
        self.create_GUI_window()
        
        
    def get_country_name(self):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")  
            sqlite_select_query = """SELECT Country from SqliteDb_developers"""  # select the speciafied col from the database
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall() 
            self.country_name_dic = {}
            self.country_name_list = []
            for row in records:
                self.country_name_dic[row[0]]=0
            for k in self.country_name_dic:
                self.country_name_list.append(k)
            #print(self.country_name_list)
            cursor.close()
            
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)        
            
        finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    
    def create_GUI_window(self):
        root = Tk()
        root.geometry("500x300")
        var = StringVar()
        menu = OptionMenu(root,var,*self.country_name_list,command=self.get_data) # command = self.function
        menu.place(x=1,y=1)
        root.mainloop()    
        
    def startClient(self):
        self.c = socket.socket()
        # if this will be an error, then use gethostbyname('localhost')
        self.c.connect((socket.gethostname(),4999))
         
    def get_data(self,name):
        self.c.send(name.encode())
        # msg is string, which means the received message from server is json/ string / string dictionary
        msg = self.c.recv(1024).decode()# listen the message from server
        
        msg_dic = json.loads(msg) 
             
        print('printing the msg: ', msg_dic)     
        
        # Draw the graph
        x_axis_list = list(msg_dic.keys()) 
        y_axis_list = list(msg_dic.values()) 

        fig= plt.figure(figsize=(15,6)) # change the size of the figure
        
        plt.title(name)
        plt.plot(x_axis_list,y_axis_list) 
        plt.show()
        
    def disconnected(self):
        # disconnected both server and client
        self.c.send('break'.encode())
        self.c.close()
        print('disconnect with the server')

GUI_obj = GUI()
GUI_obj.disconnected()