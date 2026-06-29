import random

questions = [
    {
        "question": "What is the capital of India?",
        "answer": "Delhi"
    },
    {
        "question": "Who developed Python?",
        "answer": "Guido van Rossum"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "Jupiter"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "answer": "Au"
    }
]

score = 0  

print("welcome to the quiz game!")

for question in questions:
    print(question["question"])
    answer = input("enter your answer : ")
    if answer.lower() == question["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print("next question ")


print(f"Your final score is: {score}/{len(questions)}")
