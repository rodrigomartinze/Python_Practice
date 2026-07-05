import random
from sklearn.linear_model import LinearRegression
import numpy as np

hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
exam_score = np.array([45, 52, 61, 68, 74, 79, 83, 88, 92, 97])


model = LinearRegression()
model.fit(hours_studied, exam_score)

hours = int(input("How many hours do you daily study?"))

questions = [
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What is 10 / 2?", "answer": "5"},
    {"question": "What is 3 * 4?", "answer": "12"},
    {"question": "What is 15 - 7?", "answer": "8"},
    {"question": "What is 2 ** 3?", "answer": "8"},
]

selected = random.sample(questions, 3)
correct = 0

prediction = model.predict([[hours]])
final_score = min(prediction[0], 100)
print(f"Predicted score after {hours} hours: {final_score:.2f}")
