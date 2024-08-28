from operator import truediv


class Quiz_brain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer =input(f"Q.{self.question_number}: {current_question.text}")
        correct_answer = current_question.answer
        self.check_answer(user_answer,correct_answer)

    def check_answer(self,user_answer,correct):
        if user_answer.lower() == correct.lower():
            self.score += 1
            print(f"You got it right! Your score is {self.score}/{self.question_number}")
        else:
            print(f"You got it wrong! Your score is {self.score}/{self.question_number}")
