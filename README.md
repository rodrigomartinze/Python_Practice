# Python for AI — Learning Path

A hands-on Python learning journey focused on **Machine Learning and AI development**.
Built from scratch, concept by concept, with real projects at every step.

---

## Roadmap

 Variables & Lists | ✅ |
 For Loops         | ✅ |
 Functions         | ✅ |
 Dictionaries      | ✅ |
 NumPy             | ✅ |
 Pandas            | ✅ |
 Matplotlib        | ✅ |
 Scikit-learn      | ✅ |
 ---

## 📦 Libraries Used

- **NumPy** — math operations on arrays
- **Pandas** — data manipulation and DataFrames
- **Matplotlib** — data visualization
- **Scikit-learn** — machine learning models

---

## 🚀 Projects

### 🔢 Model Accuracy Analyzer
`numpy/model_accuracy_analyzer.py`

Analyzes AI model accuracy scores using NumPy arrays.
- Calculates mean, max, and min accuracy
- Counts models above a threshold
- Finds the best model using `argmax()`

```python
accuracy_scores = np.array([0.87, 0.98, 0.43, 0.67, 0.77, 0.89])
print(f"Best model: {models_name[np.argmax(accuracy_scores)]}")
```

---

### 📊 AI Models Dashboard
`pandas/ai_dashboard.py`

Explores AI model data using Pandas DataFrames.
- Filters models by company
- Sorts by accuracy
- Finds the best performing model

```python
df[df["accuracy"] > 0.90]                        # filter high performers
df.sort_values("accuracy", ascending=False)       # sort best to worst
```

---

### 📈 Matplotlib Performance Dashboard
`matplotlib/matplotlib_dashboard.py`

Visualizes AI model data with two charts:
- **Bar chart** — compares model accuracies
- **Line graph** — shows training progress over epochs

---

### 🤖 Student Exam Score Predictor
`sklearn/sklearn_ai.py`

A Machine Learning model that predicts a student's exam score based on:
- Daily study hours (supports `1h` or `90m` format)
- Math quiz score (10 random questions)
- Penalty rules for very low quiz scores

```python
model = LinearRegression()
model.fit(X, exam_score)
prediction = model.predict([[hours, quiz_score]])
```

---

## ⚙️ Setup

```bash
# Clone the repo
git clone https://github.com/rodrigomartinze/Python_Practice.git

# Install dependencies
pip install numpy pandas matplotlib scikit-learn
```

---

## 👨‍💻 About

Built as part of a personal AI development learning path.
Goal: become an AI Developer with a focus on Machine Learning and language models.
