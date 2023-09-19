student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

def grade(score):
    if score<=100 and score>=91:
        return "outstanding"
    elif score<=90 and score>=81:
        return "exceeds expectations"
    if score<=80 and score>=71:
        return "acceptable"
    if score<=70:
        return "fail"
for student in student_scores:
    score=student_scores[student]
    student_grades[student]=grade(score)
    
print(student_grades)