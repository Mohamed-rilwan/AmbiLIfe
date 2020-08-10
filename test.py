from tkinter import *


root = Tk()
root.geometry("300x300")
root.configure(background='deepsky blue') 
root.title("Location") 
label_1 = Label(root , text="spacer")

mb = Menubutton(root, text= "Choose Ambulance Location")
mb.menu= Menu(mb)
mb["menu"]=mb.menu
mb.grid(row=4,column=1)
mb.menu.add_command(label ="Silkboard" , command=lambda: printSomething("Choosen location for demo is Silkboard Signal"))
mb.menu.add_command(label ="Marathahalli" , command=lambda: printSomething("Choosen location for demo is Marathalli Signal"))

label_2 = Label(root , text="spacer")
mb.pack()


def printSomething(x):
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()    
        label = Label(root, text= x)
    # this creates x as a new label to the GUI
        label.pack() 

root.mainloop()
root.quit()
