from sklearn.linear_model import LinearRegression
import numpy as np

hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
exam_score = np.array([45, 52, 61, 68, 74, 79, 83, 88, 92, 97])


model = LinearRegression()
model.fit(hours_studied, exam_score)

prediction = model.predict([[10]])
final_score = min(prediction[0], 100)
print(f"Predicted score after 10 hours: {final_score:.2f}")
