from tkinter import *
root =  Tk()
root.title("Python GUI")
root.geometry("500x500")
label1 = Label(root,text="i am rudal").grid(row=0,column=0)

label2 = Label(root,text="I am rudal kunwar")
label2.grid(row=10,column=10)

def clickHandeler():
   userin = e.get()
   label = Label(root,text="Hello "+userin)
   label.grid()
    
btn1 = Button(root,text="Click Me",bg="blue",fg="white",command=clickHandeler).grid(row=2,column=3)


# input field
e = Entry(root,width=50,bg="skyblue",fg="black")
e.grid()



root.mainloop()