numbers=[1,2,3,4]
new_num=[n+1 for n in numbers]
print(new_num)

name="angela"
new_list=[letter for letter in name]
print(new_list)

new=[n*2 for n in range(1,5)]
print(new)

names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names=[name for name in names if len(name)<5]
upper_names=[name.upper() for name in names if len(name)>5]
print(short_names)
print(upper_names)

import random
student_scores={name:random.randint(1,100) for name in names}
passed_students={name:score for (name,score) in student_scores.items() if score>60}
print(student_scores)
print(passed_students)

# to iterate over pandas dataframes
import pandas 
student_dict={
    "student":["angela","james","lily"],
    "score":[56,76,98]
}
#looping through dictionaries:
#for (key:value) in student_dict.items():
#   print(value)

df=pandas.DataFrame(student_dict)
print(df)
#iterating through rows of a dataframe
for index,row in df.iterrows():
    #index is the row number and row contains the actual data
    print(index)
    print(row)
    print(row.score)