from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

timer = 12

while timer > 0:
    for x in question_data:
        x_text = x['text']
        x_answer = x['answer']
        question = Question(x_text, x_answer)
        question_bank.append(question)
        timer -= 1

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("all questions were answered.")
if quiz.score > (int(quiz.question_number)/2):
    print(f"way to go! Your total score is {quiz.score}/{quiz.question_number}.")
else:
    print(f"better luck next time, your score is {quiz.score}/{quiz.question_number}.")
