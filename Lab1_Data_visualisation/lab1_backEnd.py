import re
from collections import namedtuple, defaultdict

class Import_data:
    
    def __init__(self,*args):
        self.file1 = args[0]
        self.regular_expression = args[1]
        self.open_files()
        
    def open_files(self):
        temp_text = open(self.file1,'r')    
        self.getData(temp_text)  # call the functions use self. 不然相当于这个 def 没有被按开始键
        self.average31()
        self.extractYear()
        self.getTuple()
        self.getYearXaxis_list()
        self.calculate_y_list()
        self.y_axis_min_max()
        
    def extract_number(self,text):   
        # RegExp
        r = re.findall(self.regular_expression, text)
        
        return r
    
    def getData(self,temp_text):
        
        self.temp_list = [self.extract_number(line) for line in temp_text if len(self.extract_number(line)) > 2]
    
    
    
    def average31(self):
        sum_31_years = 0
        for i in self.temp_list[110:141]:
            sum_31_years += float(i[1])
        
        self.average_31 = sum_31_years/31
    
    def extractYear(self):
        self.yearly_temp_list = []
        for m in range(len(self.temp_list)):
            self.yearly_temp_list.append(self.temp_list[m][1])
    
    def getTuple(self):
        temp = namedtuple('temp','temp')
        
        self.temp_dic = defaultdict(lambda: Empty)
        year = 1850
        
        for i in range(len(self.yearly_temp_list)):
            self.temp_dic[year] = temp(self.yearly_temp_list[i])
            year+=1                    
    
    def getYearXaxis_list(self):
        self.xaxis_year_list = []
        for i in range(len(self.temp_list)):
            self.xaxis_year_list.append(self.temp_list[i][0])
            
    # get the years value for x axis     
    def get_year_xaxis_list(self):
        return self.xaxis_year_list
    
    def calculate_y_list(self):
        self.yaxis_list = [round(float(x) - self.average_31,3) for x in self.yearly_temp_list]
                  
    def get_y_axis_list(self):
        return self.yaxis_list
    
    def y_axis_min_max(self):
        self.ymin = min(self.yaxis_list)
        self.ymax = max(self.yaxis_list)
    
    def get_y_axis_min(self):
        return self.ymin
    
    def get_y_axis_max(self):
        return self.ymax
             

# creat this function so we can get the data from outside of the class
    def get_bigger_than_Average_list(self):   #-------------- Why we dont have to put this func at def openfile():
        return self.bigger_than_average_list
    
    def get_co2_from_dic (self,year):    
        return self.co2_temp_dic[year].co2
    
    def get_temp_from_dic (self,year):
        return self.co2_temp_dic[year].temp