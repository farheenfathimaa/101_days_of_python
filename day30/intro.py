#FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# dict={"key":5}
# value=dict["non_existing_key"]

#IndexError
# list=[1,2,3]
# print(list[4])

#TypeError
# num="7"
# print(num+7)

# try:
#     file=open("a_file.txt")
#     dict={"key":5}
#     print(dict["key"])

# except FileNotFoundError:
#     file=open("a_file.txt","w")
#     file.write("Hello World!")

# except KeyError as error_message:
#     print(f"The key {error_message} does not exist in the dictionary.")

# else:
#     content=file.read()
#     print(content)

# finally:
#     # file.close()
#     # print("File was closed")
#     raise TypeError("This is an error i made")

#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)