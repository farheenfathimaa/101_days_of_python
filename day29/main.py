from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    # Use extend instead of append to add individual characters to the password_list
    password_list.extend([choice(letters) for _ in range(nr_letters)])
    password_list.extend([choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([choice(numbers) for _ in range(nr_numbers)])

    shuffle(password_list)

    p = "".join(password_list)
    pass_entry.insert(0,p)
    pyperclip.copy(p)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    new_data={
                website: {
                    "Username":username,
                    "Password":password
                }
            }
    
    if website=="" or password=="":
        messagebox.showerror(title="Oops!", message="Some fields are empty.")
    
    else:
        # try:
        #         with open("data.json", "r") as data_file:
        #             # Try to load existing data
        #             data = json.load(data_file)
        #     except (json.JSONDecodeError, FileNotFoundError):
        #         # If file is empty or not found, initialize with an empty dictionary
        #         data = {}

        #     # Update the old data with new data
        #     data.update(new_data)

        #     with open("data.json", "w") as data_file:
        #         # Save the updated data
        #         json.dump(data, data_file, indent=4)
        #         web_entry.delete(0,END)
        #         pass_entry.delete(0,END)


        is_ok= messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {username} \nPassword: {password}\nIs this ok to save?")
        if is_ok:
            try:
                with open("data.json") as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Creating a new file if it doesn't exist
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                # Clearing entries
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
            
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")
    else:
        if website in data:
            username = data[website]["Username"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website,message=f"Email: {username}\nPassword: {password}")
        else:
            messagebox.showerror(website,message='This website was not found in data')

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
web_entry=Entry(width=36)
web_entry.focus()
web_entry.grid(column=1,row=1)

username_label=Label(text="Email/Username:")
username_label.grid(column=0,row=2)
user_entry=Entry(width=55)
# to add a default value we can use insert
# user_entry.insert(index *0 for adding text at starting position and END for ending position*, "text to display")
user_entry.grid(column=1,row=2,columnspan=2)
user_entry.insert(0,"example@gmail.com")

pass_label=Label(text="Password:")
pass_label.grid(column=0,row=3)
pass_entry=Entry(width=36)
pass_entry.grid(column=1,row=3)

gen_button=Button(text="Generate Password",command=generate_password)
gen_button.grid(column=2,row=3)

add_button=Button(text="Add",width=47,command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text="Search",width=14,command=search)
search_button.grid(column=2,row=1,columnspan=1)

window.mainloop()