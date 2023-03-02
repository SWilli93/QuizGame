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
quiz.next_question()

