import random
from sklearn.linear_model import LinearRegression
import numpy as np

while True:
    user_input = input(
        "How many time do you daily study? for example 10m or 1h:  "
    ).lower()

    if "m" in user_input:
        minutes = float(user_input.replace("m", ""))
        hours = minutes / 60
        print(f"converting {minutes} minutes -> {round(hours, 2)} hours")
        break
    elif "h" in user_input:
        hours = float(user_input.replace("h", ""))
        break
    else:
        print("Please write the time correctly — example: 10m or 1h")


questions = [
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What is 10 / 2?", "answer": "5"},
    {"question": "What is 3 * 4?", "answer": "12"},
    {"question": "What is 15 - 7?", "answer": "8"},
    {"question": "What is 2 ** 3?", "answer": "8"},
    {"question": "What is 9 + 6?", "answer": "15"},
    {"question": "What is 20 / 4?", "answer": "5"},
    {"question": "What is 7 * 3?", "answer": "21"},
    {"question": "What is 100 - 45?", "answer": "55"},
    {"question": "What is 4 ** 2?", "answer": "16"},
]

selected = random.sample(questions, 5)
correct = 0


for q in selected:
    answer = input(q["question"] + " ")
    if answer == q["answer"]:
        correct += 1
        print("Correct")
    else:
        print("Incorrect")

quiz_score = correct / len(selected)
print(f"Your quiz score: {quiz_score:.0%}")


hours_quiz = np.array(
    [
        [0.1, 0.20],
        [0.2, 0.30],
        [0.3, 0.35],
        [0.5, 0.40],
        [0.6, 0.50],
        [0.8, 0.60],
        [1.0, 0.70],
        [1.1, 0.75],
        [1.3, 0.85],
        [1.5, 0.95],
        # EDGE CASES
        [1.5, 0.00],
        [0.1, 0.95],
        [0.5, 0.00],
    ]
)
exam_score = np.array([30, 38, 45, 52, 61, 68, 75, 82, 90, 97, 40, 65, 25])


model = LinearRegression()
model.fit(hours_quiz, exam_score)

prediction = model.predict([[hours, quiz_score]])
final_score = min(prediction[0], 100)
print(f"Predicted exam score : {final_score:.2f}")
