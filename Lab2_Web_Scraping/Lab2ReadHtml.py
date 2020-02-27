from bs4 import BeautifulSoup
import requests
import urllib.request
import re

class Read_html:
    def __init__(self,web_address):
        sauce = urllib.request.urlopen(web_address) 
        self.soup = BeautifulSoup(sauce,'lxml')
        self.find_table()

        
    def find_table(self):
        self.table_list = []        
        table_ul = self.soup.find('table')
        table_rows = table_ul.find_all('tr')
        
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            if len(row)==8: 
                r = re.findall("[A-Z].*([A-Z].*)*",row[0]) # return a list
                row[0] = r[0]                               
                self.table_list.append(row)
        
    def get_table(self):
        return self.table_list