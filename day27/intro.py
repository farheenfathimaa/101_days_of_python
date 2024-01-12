# from tkinter import *
# window=Tk()
# window.title("My first GUI program")
# window.minsize(width=500,height=300)

# #label
# my_label=Label(text="I am a label", font=("Times New Roman",24))
# my_label.pack()

# my_label["text"]="New text"
# my_label.config(text="New text")


# #Button
# def click_me():
#     print("I got Clicked!")
#     new_text=input.get()
#     my_label.config(text=new_text)

# button=Button(text="Click Me!", command=click_me)
# button.pack()

# #entry
# # input = Entry(width=10)
# # input.pack()
# # print(input.get())

# input = Entry(width=10)
# input.pack()


# window.mainloop()

from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)









window.mainloop()