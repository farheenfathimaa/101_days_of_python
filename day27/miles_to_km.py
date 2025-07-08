from tkinter import *
window=Tk()
window.title("Mile to KM Convertor")
window.minsize(width=250,height=150)
window.config(padx=30,pady=30)

l1=Label(text="Miles",font=("Times New Roman",14))
l1.grid(column=2,row=0)


l2=Label(text="KM",font=("Times New Roman",14))
l2.grid(column=2,row=1)


l3=Label(text="is equal to",font=("Times New Roman",14))
l3.grid(column=0,row=1)


e1=Entry(width=10)
e1.grid(column=1,row=0)

def convert():
    mile=e1.get()
    km=round(float(mile)*1.60934)
    l4.config(text=f"{km}", font=("Times New Roman",14))
    
l4=Label(text="0", font=("Times New Roman",14))
l4.grid(column=1, row=1)

b1=Button(text="Calculate",font=("Times New Roman",14), command=convert)
b1.grid(column=1,row=2)

window.mainloop()