import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


l=''
s=''
n=''
password_list=[]
for let in range(1,int(nr_letters)+1):
  l=random.choice(letters)
  let= password_list.append(l)
for sym in range(1,int(nr_symbols)+1):
  s=random.choice(symbols)
  sym= password_list.append(s)
for num in range(1,int(nr_numbers)+1):
  n=random.choice(numbers)
  num= password_list.append(n)
random.shuffle(password_list)
pw1=''
for pw in password_list:
  pw1+=pw
print(pw1)