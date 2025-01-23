question = "What is the capital of France?"
print(question)
user_answers = input("Your answer: ")
if user_answers. lower() == "paris":
    print("Correct!")
else:
    print("Oops! The correct answer is paris")
    score = 0
    score += 1
print(f"Your score is: {score}")
 
 
quiz_questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "Who wrote 'To kill a Mockingbird'?"
]
quiz_answers = [
    "paris",
    "jupiter",
    'harper lee'
]
for question in quiz_questions:
    print(f"Question: {question}")
 
import random
with open('questions.txt', 'r') as file:
    question = file.readlines()
random_line_number = random.randint(0, len(question) - 1)
random_question = question[random_line_number].strip()
print(f"Question: {random_question}")
score = 5
with open('score.txt', 'w') as file:
    file.write(f'{score}\n"')
print("score has been written to score.txt")
