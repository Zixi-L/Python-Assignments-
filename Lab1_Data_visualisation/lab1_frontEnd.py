from tkinter import*
from linearRegression import Linear_Regression
from xyPlot import Xy_plot_graph
from barChart import Bar_chart_graph


def xyPlot(event):  # even: state has changes, may buttom clicked, mouse moved
    widget = event.widget
    selection = widget.curselection() # 
    value = widget.get(selection[0]) # selection has many info, and [0] is the one we use
 
    if value =='XY Plot':
        Xy_plot_graph()
       
    elif value == 'Linear Regression':
        Linear_Regression()
    
    else:
        Bar_chart_graph()
        
    
master = Tk()
master.geometry("500x300")
master.title('Please choose a graph')
        
lbox=Listbox(master, background="white", fg="black",selectbackground="blue",highlightcolor="black")
lbox.grid(row=1, column=1)
lbox.insert("end", "XY Plot")
lbox.insert("end", "Linear Regression")
lbox.insert("end", "Bar Chart")
lbox.bind("<Double-Button-1>", xyPlot)

lbox.pack(side="top", fill="both", expand=True)

master.mainloop()