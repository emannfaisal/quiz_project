from question import question_data
from question_model import Question
from quiz_brain import Quiz_brain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = Quiz_brain(question_bank)

while quiz.still_question():
    quiz.next_question()

print(f"You have completed the quiz")
print(f"Your score is {quiz.score}")
