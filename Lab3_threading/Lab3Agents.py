from queue import Queue
import threading
import time
import sqlite3

class Agents(threading.Thread): #this makes the class a threading class
    def __init__(self,agent_id, thread_lock):
        threading.Thread.__init__(self)  # to initialise Thread class
        self.agent_id = agent_id
        self.cols_dic = {1:'CO2', 2:'CH4' , 3:'N2O' , 4:'CFC12', 5:'CFC11', 6:'_15minor'}
        self.thread_lock = thread_lock
        self.q = Queue()
        
 
    def wait(self):  # for the use of threading class
        time.sleep(.2)
        
    def run(self):    # for the use of threading class
        for year in range(1979,2019):
            self.get_data(year)
        
    def get_data(self,year):
        with self.thread_lock:  # starts with lock, ends with lock releasing , self.thread_lock makes the func. thread safe
            try:
                sqliteConnection = sqlite3.connect('SQLite_Python.db')
                cursor = sqliteConnection.cursor()
                print("Connected to SQLite")
                
                sqlite_select_query = "SELECT {0} from SqliteDb_developers WHERE Year = '{1}'".format(self.cols_dic[self.agent_id],year) # select all the cols from the database
                
                cursor.execute(sqlite_select_query)
                records = cursor.fetchall()
                self.q.put(float(records[0][0]))  # put(element) keep adding one element into the queue each time
                print('Agent',self.agent_id,'consuming',year)
                cursor.close()
        
            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("The SQLite connection is closed")        
        
def main():
    lock = threading.Lock()
    agent_list = []
    
    for agent_id in range(1,7):
        agent_list.append(Agents(agent_id,lock))
        agent_list[-1].start()
    
    for agent in agent_list:
        agent.join()
        
main()
        
        
        
        
#lock = threading.Lock()

#agent_list=[]

#for agent_id in range(1,7):
    #agent_list.append(Agents(agent_id,lock))
    #agent_list[-1].start()

#for agent in agent_list:
    #agent.join()