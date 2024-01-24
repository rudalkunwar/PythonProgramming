from tkinter import *

root = Tk()

root.title("Calculator")
root.geometry("700x650")


input = Entry(root,width=40,font=('Arial', 20))
input.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

# buttons = [
#      '0', '1', '2', '3',
# 0     [                 ]
# 1     '7', '8', '9', '/',
# 2     '4', '5', '6', '*',
# 3     '1', '2', '3', '-',
# 4     '0', '.', '=', '+'
# 

def button_click(number):
    current = input.get()
    input.delete(0,END)
    input.insert(0,str(current)+str(number))
    global operation
    operation = str(current)+str(number)

def clear():
    input.delete(0,END)

def equal():
    value = eval(operation)
    input.delete(0,END)
    input.insert(0,value)


btndot = Button(root,text="Clear",padx=20,pady=20,command=clear)
btndot.grid(row=4,column=1,padx=20,pady=20)

btnmul = Button(root,text="x",padx=20,pady=20,command=lambda: button_click('*'))
btnmul.grid(row=2,column=3,padx=20,pady=20)

btndiv = Button(root,text="/",padx=20,pady=20,command=lambda: button_click('/'))
btndiv.grid(row=1,column=3,padx=20,pady=20)

btnsub = Button(root,text="-",padx=20,pady=20,command=lambda: button_click('-'))
btnsub.grid(row=3,column=3,padx=20,pady=20)

btnadd = Button(root,text="+",padx=20,pady=20,command=lambda: button_click('+'))
btnadd.grid(row=4,column=3,padx=20,pady=20)

btnequal = Button(root,text="=",padx=20,pady=20,command=equal)
btnequal.grid(row=4,column=2,padx=20,pady=20)

btn0 = Button(root,text="0",padx=20,pady=20,command=lambda: button_click(0))
btn0.grid(row=4,column=0,padx=20,pady=20)

btn1 = Button(root,text="1",padx=20,pady=20,command=lambda: button_click(1))
btn1.grid(row=3,column=0,padx=20,pady=20)

btn2 = Button(root,text="2",padx=20,pady=20,command=lambda:button_click(2))
btn2.grid(row=3,column=1,padx=20,pady=20)

btn3 = Button(root,text="3",padx=20,pady=20,command=lambda:button_click(3))
btn3.grid(row=3,column=2,padx=20,pady=20)

btn4 = Button(root,text="4",padx=20,pady=20,command=lambda:button_click(4))
btn4.grid(row=2,column=0,padx=20,pady=20)

btn5 = Button(root,text="5",padx=20,pady=20,command=lambda:button_click(5))
btn5.grid(row=2,column=1,padx=20,pady=20)

btn6 = Button(root,text="6",padx=20,pady=20,command=lambda:button_click(6))
btn6.grid(row=2,column=2,padx=20,pady=20)

btn7 = Button(root,text="7",padx=20,pady=20,command=lambda:button_click(7))
btn7.grid(row=1,column=0,padx=20,pady=20)

btn8 = Button(root,text="8",padx=20,pady=20,command=lambda:button_click(8))
btn8.grid(row=1,column=1,padx=20,pady=20)

btn9 = Button(root,text="9",padx=20,pady=20,command=lambda:button_click(9))
btn9.grid(row=1,column=2,padx=20,pady=20)






root.mainloop()