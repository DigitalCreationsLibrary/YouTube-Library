from tkinter import Tk, Checkbutton, Button, Label
from tkinter import IntVar

main_window = Tk()
main_window.geometry ('800x400+250+200')
main_window.title("Checkbutton")


var = IntVar()

labVal = Label(main_window, text="", bg="white", fg="green", font=("Times",12))
labVal.pack(pady=10)

def getValue():
   labVal["text"] = str(var.get() )


chB = Checkbutton(main_window, variable=var, text="I am A check button",font=("Times",12))
chB.pack(pady=50)

getVB = Button(main_window, text="Get The Value",font=("Times",12), bg="green", fg="white", command=getValue,)
getVB.pack(pady=50)


main_window.mainloop()



