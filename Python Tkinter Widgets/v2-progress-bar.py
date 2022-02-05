from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter.messagebox import showinfo
from random import random

main_window = ThemedTk(theme="scidpurple")
#main_window = tk.Tk()
main_window.geometry('700x400+400+200')
main_window.title("a Progress Bar")
theProgBar = ttk.Progressbar(main_window,orient='horizontal', mode='determinate',length=500, maximum = 100)
theProgBar.grid(column=0, row=0,padx=10,pady=10)

labelProg = ttk.Label(main_window, text="0%")
labelProg.grid(column=1, row=0,padx=10,pady=10)


liFrame =ttk.Frame(main_window, width=40,height=10)
liFrame.grid(column = 0, row = 2, padx=10,pady=10)
scrollbar = ttk.Scrollbar(liFrame)
theList = tk.Listbox(liFrame,width=50,heigh=15,yscrollcommand=scrollbar.set)
scrollbar.configure(command=theList.yview)
theList.pack (side="left")
scrollbar.pack(side="right", fill="y")   


def aProcess():

    aList =[]
    for i in range (100):
        k = 0
        for j in range (50000):
            k = k + random()        
        aList.append(k)
        theProgBar['value'] = theProgBar['value']+1
        theProgBar.update_idletasks()
        labelProg['text'] = str(i+1) + " %"
        theList.insert('end',k)    
    showinfo(message='The Process is completed!')
    
    
calcButton = ttk.Button(main_window, text='Start the process',command=aProcess)
calcButton.grid (column = 0, row = 1,padx=10,pady=10)    


main_window.mainloop()   
