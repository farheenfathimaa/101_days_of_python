from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for q in question_data:
    qtext=q["text"]
    qanswer=q["answer"]
    question=Question(qtext,qanswer)
    question_bank.append(question)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")