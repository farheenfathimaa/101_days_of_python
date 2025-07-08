# PLACEHOLDER="[name]"

# #TODO: Create a letter using starting_letter.txt 
# with open(".\Input\Letters\starting_letter.txt") as starting_letter:
#     letter=starting_letter.readlines()
# #for each name in invited_names.txt
# with open(".\Input\Names\invited_names.txt") as invited_names:
#     names=invited_names.read()
# #Replace the [name] placeholder with the actual name.
# with open(".\Input\Letters\starting_letter.txt","a") as starting_letter:
#     for name in names:
#         stripped_name=name.strip()
#         new_letter=letter.replace(PLACEHOLDER,stripped_name.name)
#         with open(f".\Output\ReadyToSend\letter_for_{stripped_name}.txt",mode="w") as completed_letter:
#             completed_letter.write(new_letter)
# #Save the letters in the folder "ReadyToSend".
    
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

# TODO: Create a letter using starting_letter.txt
with open(r".\Input\Letters\starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

# For each name in invited_names.txt
with open(r".\Input\Names\invited_names.txt") as invited_names:
    names = invited_names.readlines()

# Replace the [name] placeholder with the actual name and save the letters
for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace(PLACEHOLDER, stripped_name)
    
    output_path = rf".\Output\ReadyToSend\letter_for_{stripped_name}.txt"
    
    with open(output_path, mode="w") as completed_letter:
        completed_letter.write(new_letter)

# Save the letters in the folder "ReadyToSend".
