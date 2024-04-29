import tkinter as tk 

calculation =""

def enter_value(symbol):
    global calculation
    calculation+=str(symbol)
    text_res.delete(1.0,"end")
    text_res.insert(1.0,calculation)
    
def calculate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_res.delete(1.0,"end")
        text_res.insert(1.0,calculation)
    except:
        clear()
        text_res.insert(1.0,"Error")
    
def clear():
    global calculation
    calculation=""
    text_res.delete(1.0,"end")
    
    
    
root = tk.Tk()
root.geometry("300x275")
text_res = tk.Text(root,height=2,width=16, font=("Arial",24))
root.title("Calculator")
text_res.grid(columnspan=5)

btn1 = tk.Button(root,text="1", command=lambda: enter_value(1),width=5, font=("Arial",14))
btn1.grid(row=2,column=1)
btn2 = tk.Button(root,text="2", command=lambda: enter_value(2),width=5, font=("Arial",14))
btn2.grid(row=2,column=2)
btn3 = tk.Button(root,text="3", command=lambda: enter_value(3),width=5, font=("Arial",14))
btn3.grid(row=2,column=3)
btn4 = tk.Button(root,text="4", command=lambda: enter_value(4),width=5, font=("Arial",14))
btn4.grid(row=3,column=1)
btn5 = tk.Button(root,text="5", command=lambda: enter_value(5),width=5, font=("Arial",14))
btn5.grid(row=3,column=2)
btn6 = tk.Button(root,text="6", command=lambda: enter_value(6),width=5, font=("Arial",14))
btn6.grid(row=3,column=3)
btn7 = tk.Button(root,text="7", command=lambda: enter_value(7),width=5, font=("Arial",14))
btn7.grid(row=4,column=1)
btn8 = tk.Button(root,text="8", command=lambda: enter_value(8),width=5, font=("Arial",14))
btn8.grid(row=4,column=2)
btn9 = tk.Button(root,text="9", command=lambda: enter_value(9),width=5, font=("Arial",14))
btn9.grid(row=4,column=3)
btn0 = tk.Button(root,text="0", command=lambda: enter_value(0),width=5, font=("Arial",14))
btn0.grid(row=5,column=2)
btnplus = tk.Button(root,text="+", command=lambda: enter_value("+"),width=5, font=("Arial",14))
btnplus.grid(row=2,column=4)
btnminus = tk.Button(root,text="-", command=lambda: enter_value("-"),width=5, font=("Arial",14))
btnminus.grid(row=3,column=4)
btnmultiply = tk.Button(root,text="*", command=lambda: enter_value("*"),width=5, font=("Arial",14))
btnmultiply.grid(row=4,column=4)
btndiv = tk.Button(root,text="/", command=lambda: enter_value("/"),width=5, font=("Arial",14))
btndiv.grid(row=5,column=4)
btnopen = tk.Button(root,text="(", command=lambda: enter_value("("),width=5, font=("Arial",14))
btnopen.grid(row=5,column=1)
btncl = tk.Button(root,text=")", command=lambda: enter_value(")"),width=5, font=("Arial",14))
btncl.grid(row=5,column=3)
btnexp = tk.Button(root,text="^", command=lambda: enter_value("**"),width=5, font=("Arial",14))
btnexp.grid(row=6,column=2)
btndec = tk.Button(root,text=".", command=lambda: enter_value("."),width=5, font=("Arial",14))
btndec.grid(row=6,column=3)
btnequals = tk.Button(root, text="=", command=calculate, width=5, font=("Arial",14),bg="red",fg="black")
btnequals.grid(row=6,column=4)
btnclear = tk.Button(root, text="C", command=clear, width=5, font=("Arial",14),bg="orange",fg="black")
btnclear.grid(row=6,column=1,columnspan=1)
root.mainloop()
    
