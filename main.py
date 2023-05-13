from question_model import Question
from all_data.data import question_data
from quiz_brain import QuizBrain
game_is_on = True
question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("\nYou`ve completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")