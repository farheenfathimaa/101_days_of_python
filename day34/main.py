# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
# from ui import UserInterface

# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)


# quiz = QuizBrain(question_bank)
# quiz_ui=UserInterface(quiz)
# # while quiz.still_has_questions():
# #     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import UserInterface

# Check if question_data is empty before creating question_bank and quiz
if question_data:
    question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]
    quiz = QuizBrain(question_bank)
    quiz_ui = UserInterface(quiz)

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
else:
    print("Failed to fetch questions. Check your network connection.")
