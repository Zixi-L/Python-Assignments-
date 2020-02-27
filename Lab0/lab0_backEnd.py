import re
from collections import namedtuple, defaultdict

class Import_data:
    
    def __init__(self,*args):
        self.file1 = args[0]
        self.file2 = args[1] 
        self.regular_expression = args[2]
        self.open_files()
        
    def open_files(self):
        co2_text = open (self.file1,'r')
        temp_text = open(self.file2,'r')    
        self.getData(co2_text, temp_text)  # call the functions use self.
        self.calculateAverageEachYear()
        self.average31()
        self.extractYear()
        self.getTuple()
        self.aboveBlow()
        
        
    def extract_number(self,text):   
        # RegExp
        r = re.findall(self.regular_expression, text)
        
        return r
    
    def getData(self,co2_text,temp_text):
        self.co2_list = [self.extract_number(line) for line in co2_text if len(self.extract_number(line)) > 2]  # Comprehension
                
        self.temp_list = [self.extract_number(line) for line in temp_text if len(self.extract_number(line)) > 2]
    
    
    def calculateAverageEachYear(self):
        self.yearly_co2_list = []
        
        count = 0
        while count < 730:
            m = 1
            total = 0.00
            while m <= 12:
                total += float(self.co2_list[count][3])
                m += 1
            count += 12
            total = round(total/12,2)  
            self.yearly_co2_list.append(total)
    
    def average31(self):
        sum_31_years = 0
        for i in self.yearly_co2_list[1:32]:
            
            sum_31_years += i
            
        self.average_31 = sum_31_years/31
    
    def extractYear(self):
        self.yearly_temp_list = []
        for m in range(110, len(self.temp_list)):
            self.yearly_temp_list.append(self.temp_list[m][1])
        
    def getTuple(self):
        co2_temp = namedtuple('co2_temp','co2 temp')
        
        self.co2_temp_dic = defaultdict(lambda: Empty)
        year = 1960
                
        for i in range(len(self.yearly_temp_list)):
            self.co2_temp_dic[year] = co2_temp(self.yearly_co2_list[i], self.yearly_temp_list[i])
            year+=1                   
    
       
    def aboveBlow(self):
        self.bigger_than_average_list = []
        self.smaller_than_average_list = []
        
        for i in self.co2_temp_dic:
            if self.co2_temp_dic[i].co2 > self.average_31:
                self.bigger_than_average_list.append([i,self.co2_temp_dic[i].co2])
        
            else:
                self.smaller_than_average_list.append([i,self.co2_temp_dic[i].co2])

# creat this function so we can get the data from outside of the class
    def get_bigger_than_Average_list(self):
        return self.bigger_than_average_list
    
    def get_smaller_than_average_list(self):
        return self.smaller_than_average_list
    
    def get_co2_from_dic (self,year):
        return self.co2_temp_dic[year].co2
    
    def get_temp_from_dic (self,year):
        return self.co2_temp_dic[year].temp    