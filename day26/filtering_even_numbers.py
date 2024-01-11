# list_of_strings = input().split(',')
# # TODO: Use list comprehension to convert the strings to integers 👇:
# numbers=[int(num) for num in list_of_strings]

# # TODO: Use list comprehension to filter out the odd numbers
# # and store the even numbers in a list called "result"
# result=[num for num in numbers if num%2==0]

# print(result)


# Get input as a single string
input_string = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of strings
list_of_strings = input_string.split()

# Use list comprehension to convert the strings to integers,
# excluding empty strings
numbers = [int(num) for num in list_of_strings if num.strip()]

# Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [num for num in numbers if num % 2 == 0]

print(result)
