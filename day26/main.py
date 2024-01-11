import pandas
alphabets=pandas.read_csv("nato_phonetic_alphabet.csv")
student_data_frame = pandas.DataFrame(alphabets)

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict={row.letter:row.code for (index, row) in student_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word=input("Enter a word: ").upper()
output_list=[phonetic_dict[letter] for letter in word]
print(output_list)
