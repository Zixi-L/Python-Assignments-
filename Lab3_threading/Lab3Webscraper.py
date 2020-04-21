from bs4 import BeautifulSoup
import requests
import urllib.request
import re


class Read_html:
    def __init__(self,web_address):
        sauce = urllib.request.urlopen(web_address).read()
        self.soup = BeautifulSoup(sauce,'lxml')
        self.find_table()

        
    def find_table(self):
        self.table_list = [] 
        # we will find two tables, and we only want the second one.
        # so we can use, {'class':'table_name_from web source code'} to get the target table
        # or we can use the index to get the table
        
        table_ul = self.soup.find_all('table')
        target_table = table_ul[1]
        #print(type(target_table))
        
        table_rows = target_table.find_all('tr')
        
        for tr in table_rows:
            td = tr.find_all('td')
            if len(td)==11:
                row = [i.text for i in td]
                self.table_list.append(row)
            
        #print(self.table_list)    
        
    def get_table(self):
        return self.table_list

#obj_read_html = Read_html('https://www.esrl.noaa.gov/gmd/aggi/aggi.html')