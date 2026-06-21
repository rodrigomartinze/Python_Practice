import numpy as np

accuracy_scores = np.array([0.76, 0.12, 0.56, 0.78, 0.99])
mean = 0
for i in accuracy_scores:
    mean += i
mean = mean / len(accuracy_scores)
print(mean)

print(accuracy_scores.max())  # → highest score
print(accuracy_scores.min())  # → lowest score
print(accuracy_scores > 0.85)  # → try this one and see what it prints!
print(sum(accuracy_scores > 0.85))
