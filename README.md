# 🐍 Python for AI — Learning Path

A hands-on Python learning journey focused on Machine Learning and AI development.
Built from scratch, concept by concept, with real projects at every step.

---

## 🗺️ Roadmap

| Concept | Status |
|---|---|
| Variables & Lists | ✅ |
| For Loops | ✅ |
| Functions | ✅ |
| Dictionaries | ✅ |
| NumPy | ✅ |
| Pandas | ✅ |
| Matplotlib | ✅ |
| Scikit-learn | ✅ |
| Groq AI API | ✅ |

---

## 📦 Libraries Used

- **NumPy** — math on arrays
- **Pandas** — tables and DataFrames
- **Matplotlib** — charts and graphs
- **Scikit-learn** — ML models
- **Groq** — AI API integration

---

## 🚀 Projects

### 🔢 Model Accuracy Analyzer
`numpy/model_accuracy_analyzer.py`

One of my first real projects. Takes a list of AI model accuracy scores and finds the best one using NumPy.

```python
accuracy_scores = np.array([0.87, 0.98, 0.43, 0.67, 0.77, 0.89])
print(f"Best model: {models_name[np.argmax(accuracy_scores)]}")
```

---

### 📊 AI Models Dashboard
`pandas/ai_dashboard.py`

My first time working with DataFrames. I learned how to filter, sort, and explore data — the same way data scientists do it.

```python
df[df["accuracy"] > 0.90]
df.sort_values("accuracy", ascending=False)
```

---

### 📈 Matplotlib Performance Dashboard
`matplotlib/matplotlib_dashboard.py`

Two charts in one file — a bar chart comparing model accuracies and a line graph showing training progress over epochs. First time I made data actually visual.

---

### 🤖 Student Exam Score Predictor
`sklearn/sklearn_ai.py`

My first real ML model. It predicts a student's exam score based on study hours and quiz performance. Includes a math quiz and penalty rules for very low scores.

```python
model = LinearRegression()
model.fit(X, exam_score)
prediction = model.predict([[hours, quiz_score]])
```

---

### 🧠 AI Data Analyzer
`AI_API/data_analyzer.py`

First project using a real AI API. Sends a Pandas DataFrame to Groq (Llama 3) and gets back a full analysis — topics, insights, and comparisons.

---

### 📝 AI Math Exam
`AI_API/math_exam.py`

My most complete project so far. The AI generates personalized math questions based on the student's grade level and difficulty choice. After the quiz, it analyzes the results and gives a personalized study guide.

**Features:**
- AI generates 10 questions based on grade level and difficulty
- Validates that the student can't submit empty answers
- Tracks time spent on each question (useful for detecting cheating!)
- Saves results to CSV and Excel with color-coded sheets
- AI gives a personalized study guide based on wrong answers

```python
# AI generates questions based on grade + difficulty
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": f"Generate 10 math questions for grade {grade} at {difficulty} level..."}]
)

# Timer tracks how long each answer takes
start = time.time()
answer = input(q["question"])
elapsed = round(time.time() - start, 2)

# Results saved to Excel with two sheets
export_to_excel(name, grade, difficulty, score, df_results, feedback, f"{name}_results.xlsx")
```

<img width="981" height="322" alt="image" src="https://github.com/user-attachments/assets/4a5dc554-bcfa-4123-ba49-9eb517d8671c" />

---

## ⚙️ Setup

```bash
git clone https://github.com/rodrigomartinze/Python_Practice.git
pip install numpy pandas matplotlib scikit-learn groq python-dotenv
```

Create a `.env` file in the `AI_API` folder:
```
GROQ_API_KEY=your-key-here
```

---

## 👨‍💻 About

I'm a high school student learning Python and AI from scratch with the goal of becoming an AI Developer. Every project here was built step by step, making mistakes and fixing them — that's how I actually learned.
