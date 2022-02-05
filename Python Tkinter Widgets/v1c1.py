from tkinter import font, Button, Label, Tk, messagebox
from PIL import Image, ImageTk
from datetime import datetime

#Creation of the main window
main_window = Tk()
main_window.geometry('700x400+250+200')
main_window.title("A tk Button")
main_window.configure(bg = "goldenrod")


# Creation of the label that indicates the current time
myLabel = Label(main_window,text="",font = ("Bookman",50), bg="goldenrod")
myLabel.pack()

# Creation of the 2 types of buttons
myButtonText = Button(main_window)
myButtonImg =  Button(main_window)

# a function that show a message box with the "Hello !" message
def sayHello(event = None):
   messagebox.showinfo("", "Hello !")

# a funciton that display the current time, and if the value of the minutes
# is greater then the threshold, the color of the label will be red.
# If it is not, it will be green.
def displayTime(threshold):
    now = datetime.now()
    myLabel.configure(text= now.strftime("%H:%M:%S"))
    if (now.minute > threshold):
        myLabel.configure(fg="red")
    else:
        myLabel.configure(fg="green")

# A function that set the common set of properties of the 2 buttons
def confButton(myButton,w,h,myBd,hT,myCommand,myBgColor):
	myButton.configure(activebackground = "#5a9908",
						activeforeground= myBgColor)
	myButton.configure(bg = myBgColor, fg="snow")
	myButton["highlightcolor"]="salmon"
	myButton.configure(highlightthickness =hT)
	myButton.configure(bd = myBd, relief = "raised",state= "normal")
	myButton.configure( width = w, height = h)
	myButton.configure(command = myCommand)
	myButton.bind('<Return>', myCommand)

# Setting the remaining properties for the text button
confButton(myButtonText,20,2,5,2, sayHello,"SkyBlue1")
myButtonText.configure(text="Say Hello!\nYou won't regret it!")
main_window.bind('<Alt-s>', sayHello)
myFont = font.Font (family = "Bookman", size = 16 , weight = "bold", slant = "italic", underline = 0, overstrike =0 )
myButtonText.configure(font  = myFont)
myButtonText.configure(justify  = "left")
myButtonText.configure(padx= 20 , pady = 20)
myButtonText.configure(underline= 0)
myButtonText.configure(wraplength = 200)


# Setting the remaining properties for the image button
confButton(myButtonImg,374,122,0,0,lambda event = None: displayTime(30),"goldenrod")
main_window.bind('<Alt-g>', lambda event= None: displayTime(30))
img = Image.open("bimg.png")
photo = ImageTk.PhotoImage(img)
myButtonImg.configure(image =photo , borderwidth = 0)

# Packing the 2 buttons
myButtonImg.pack(pady=20)
myButtonText.pack(pady=20)

# Running the app
main_window.mainloop()
