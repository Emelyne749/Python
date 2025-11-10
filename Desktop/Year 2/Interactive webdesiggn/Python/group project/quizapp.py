# quiz_app.py
import csv

def load_questions():
    questions = []
    with open("quiz_questions.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            questions.append({"question": row[0], "options": row[1:5], "answer": row[5]})
    return questions

def run_quiz():
    questions = load_questions()
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, opt in enumerate(q["options"], 1):
            print(f"{i}. {opt}")
        answer = input("Enter option number: ")
        if q["options"][int(answer)-1] == q["answer"]:
            score += 1
    print(f"Your score: {score}/{len(questions)}")

# Example usage: create 'quiz_questions.csv' with question, 4 options, correct answer
# quiz_questions.csv example row:
# What is 2+2?,1,2,3,4,4

run_quiz()
