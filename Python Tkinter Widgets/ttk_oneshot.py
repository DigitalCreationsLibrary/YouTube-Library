import tkinter as tk
import tkinter.ttk as ttk


# Main Window Configuration
main_window = tk.Tk()
main_window.title("TTK Widgets in One shot")
main_window.geometry("640x480+300+50")
main_window.configure(background="#086788")


s = ttk.Style()
s.configure('.',background="#FFD6AF")

s.theme_use("winnative")


# Adding the common TTK Widgets

## The Tk Frames to Group all the widgets
common_widgets= tk.Frame(main_window,bg="#086788",borderwidth=2,relief="ridge")
common_widgets.pack(padx=5,pady=5,fill="both")
tk.Frame()


## The Actual Widgets
button=ttk.Button(common_widgets,text="TTK Button",)
button.grid(padx=10,pady=5,row=0, column=0)

check_button=ttk.Checkbutton(common_widgets,text="Check Button",)
check_button.grid(padx=10,pady=5,row=0, column=1)

val= tk.StringVar()
val.set("TTK Entry")
entry=ttk.Entry(common_widgets,textvariable=val)
entry.grid(padx=10,pady=5,row=0, column=2)

frame=ttk.Frame(common_widgets,width=150, height=60)
frame.grid(padx=10,pady=5,row=0, column=3,sticky="ew")
# label_fframe = ttk.Label(frame, text="Label on Frame")
# label_fframe.pack()


label=ttk.Label(common_widgets,text="TTK Label")
label.grid(padx=10,pady=5,row=1, column=0)

label_frame=ttk.LabelFrame(common_widgets,text="TTK Label Frame",width=150, height=60)
label_frame.grid(padx=10,pady=5,row=1, column=1)

menu_button=ttk.Menubutton(common_widgets,text="TTK Menubutton")
menu_button.grid(padx=10,pady=5,row=1, column=2)
menu_button.menu=tk.Menu(menu_button,tearoff=0)
menu_button.menu.add("command",label="TTK Menu Item")
menu_button["menu"]=menu_button.menu

paned_window = ttk.PanedWindow(common_widgets,orient="horizontal",width=150, height=60)
paned_window.grid(padx=10,pady=5,row=1, column=3,sticky="ew")
# label_fpaned = ttk.Label(paned_window, text="Label on Paned_Window")
# label_fpaned.pack()

radio_button=ttk.Radiobutton(common_widgets,text="TTk Radio button",)
radio_button.grid(padx=10,pady=5,row=2, column=0)


scale=ttk.Scale(common_widgets,from_=0,to=100,orient="horizontal")
scale.grid(padx=10,pady=5,row=2, column=1)


scrollbar=ttk.Scrollbar(common_widgets,orient="horizontal",)
scrollbar.grid(padx=10,pady=5,row=2, column=2)




# Adding the new TTk Widgets
## The Tk Frame to Group all the widgets
new_widgets=tk.Frame(main_window,bg="#086788",width=450,height=200,relief="ridge",bd=2)
new_widgets.pack(padx=5,pady=5,fill="both")


# sizegrip = ttk.Sizegrip(common_widgets)
# sizegrip.grid(padx=10,pady=5,row=3, column=0)
## The Actual Widgets

combobox = ttk.Combobox(new_widgets,values=["TTK Combobox item 1","TTK Combobox item 2"])
combobox.grid(padx=10,pady=5,row=4, column=0)

notebook = ttk.Notebook(new_widgets,width=200,height=50,)
notebook.grid(padx=10,pady=5,row=4, column=1)
notebook.add(ttk.Label(notebook,text="TTK Notebook Page 1"),text="Tab 1")
notebook.add(ttk.Label(notebook,text="TTK Notebook Page 2"), text="Tab 2")

progressbar = ttk.Progressbar(new_widgets,orient="horizontal",length=200,mode="determinate",value=50)
progressbar.grid(padx=10,pady=5,row=4, column=2)
new_style = ttk.Style()
new_style.configure("any.TSeparator",background="black",foreground="white")
separator = ttk.Separator(new_widgets, orient="vertical", )

separator.grid(padx=5, pady=5, row=4, column=3, sticky="ns")

sizegrip = ttk.Sizegrip(new_widgets,)
sizegrip.grid(padx=10,pady=5,row=5, column=0)

treeview = ttk.Treeview(new_widgets,columns=("col1",),show="headings",height=5,)
treeview.heading(0,text="column 1" )
treeview.grid(padx=10,pady=5,row=5, column=1)





# adding a tk close button
close=tk.Button(main_window,text="Close",bg="#086788",relief="ridge", font=("Times",14),fg="#fff",activebackground="#FFD6AF",command=main_window.destroy,)
close.pack(padx=10,pady=5,side=tk.RIGHT)
main_window.mainloop()
