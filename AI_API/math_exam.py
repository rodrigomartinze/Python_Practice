import os
import json
import ast
from groq import Groq
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

name = input("What's your name? ")
grade = input("What's your grade level? ")


difficulty = input("Choose your difficulty: easy, medium or hard: ")
while difficulty not in ["easy", "medium", "hard"]:
    difficulty = input("Please type easy, medium or hard: ")



response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{
        "role": "user", 
        "content": f"Generate 10 math questions for a grade/level {grade} student, use a {difficulty} difficulty level . Return ONLY a JSON array like this: [{{'question': 'What is 2+2?', 'answer': '4'}}]. No extra text, just the JSON."
    }]
)

questions = ast.literal_eval(response.choices[0].message.content)
correct = 0
results = []
for q in questions:
    answer = input(q["question"] + " ")
    results.append({
        "question": q["question"],
        "student_answer": answer,
        "correct_answer": q["answer"],
        "is_correct": answer == q["answer"]
    })
    if answer == q["answer"]:
        print("Correct")
        correct += 1
    else:
        print("Incorrect")
        
score = correct / len(questions)
print(f"Your score is {score:.0%}")

df_results = pd.DataFrame(results)

summary = f"""

Here are your results {name}:
{df_results}
"""
print(summary)

feedback = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{
        "role": "user",
        "content": f"A student named {name} in grade {grade} just took a math quiz. Using these results: {summary}, tell the student which topics they need to study and give them a personalized study guide about the topics they failed."
    }]
)

print(feedback.choices[0].message.content)