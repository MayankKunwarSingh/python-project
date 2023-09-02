class Question:
    def _init_(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

def run_quiz(questions):
    score = 0
    for question in questions:
        question.display_question()
        user_answer = int(input("Enter your answer (1, 2, 3, or 4): "))
        if question.check_answer(user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question.correct_answer}.\n")
    
    print(f"You got {score}/{len(questions)} questions correct!")

# Sample questions
question1 = Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], 3)
question2 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], 2)
question3 = Question("What is 2 + 2?", ["3", "4", "5", "6"], 2)

questions = [question1, question2, question3]

# Run the quiz
run_quiz(questions)