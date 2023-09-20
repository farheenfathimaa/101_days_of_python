def format_name(f_name,l_name):
    return f_name.title(),l_name.title()
f_name=input("enter first: ")
l_name=input("enter surname: ")
Fname,Lname=format_name(f_name=f_name,l_name=l_name)
print(Fname+" "+Lname)