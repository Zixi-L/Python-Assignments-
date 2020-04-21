import socket
import json
import sqlite3

        
class Server:
    def __init__(self):
        self.server()
       
    def server(self):    
        s = socket.socket()
        s.bind((socket.gethostname(),4999))
        s.listen(1)  # how many computer it connects with
        # s.accept() returns a tuple, first assign to the sercersocket, the 2nd assigns to address.
        serversocket, address = s.accept() # these 4 lines connect to the server
        # Only connects once
        print(f'connection from {address} has been establisted!')
        
        while True:
            msg = serversocket.recv(1024).decode()
            if msg == 'break':
                break
            
            # if I declare the year_value_dic inside the try block, I cannot access from the outside of try block
            year_value_dic = {}
                  
            try:
                sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = sqliteConnection.cursor()
                print("Successfully Connected to SQLite")  
                sqlite_select_query = """SELECT * from SqliteDb_developers"""  # select the speciafied col from the database
                cursor.execute(sqlite_select_query)
                records = cursor.fetchall()
                
                for row in records:
                    if msg == row[0]:
                        year_value_dic[row[1]]=row[2]
                       
                cursor.close()
                
            except sqlite3.Error as error:
                print("Failed to insert Python variable into sqlite table", error)        
                
            finally:
                    if (sqliteConnection):
                        sqliteConnection.close()                    
            
            data_json = json.dumps(year_value_dic)
            #bytes(msg,'utf-8')
            serversocket.send(data_json.encode())
            
        serversocket.close() 

Server_obj = Server()