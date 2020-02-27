from Lab2_Get_top_ten import Get_top_ten
import matplotlib.pyplot as plt

class Graph_pie_chart:
    def __init__(self):
        pass
    
    def calculate_size(self,l):
        sum = 0
        for i in l:
            sum += i
            
        self.sizes = []
        for s in l:
            x = round(((s*100)/sum),2)
            self.sizes.append(x)
            
    def graph_pie_chart(self,labels):
        
        fig1, ax1 = plt.subplots()
        
        explode = (0.5, 0.25, 0.45, 0.25, 0.35,0, 0, 0, 0, 0,) 
        
        ax1.pie(self.sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)    
        ax1.axis('equal') 
        
        plt.title('Fossil CO2 Emissions in 2017 (% of world) - Top ten countries')
        plt.show()    
    

def main():
    Graph_pie_chart_obj = Graph_pie_chart()
    Get_top_ten_obj = Get_top_ten()
    Graph_pie_chart_obj.calculate_size(Get_top_ten_obj.get_top_ten_Co2_data())
    Graph_pie_chart_obj.graph_pie_chart(Get_top_ten_obj.get_top_ten_labels())

main()