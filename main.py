from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

Question_bank = []
for new_q in question_data:
    question_obj = Question(new_q['text'], new_q['answer'])
    Question_bank.append(question_obj)

quiz = QuizBrain(Question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
