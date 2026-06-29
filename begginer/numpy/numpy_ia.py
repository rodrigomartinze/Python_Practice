import numpy as np

accuracy_scores = np.array([0.76, 0.12, 0.56, 0.78, 0.99])
# mean = 0
# for i in accuracy_scores:
#     mean += i
# mean = mean / len(accuracy_scores)
mean = accuracy_scores.mean()
print(mean)

print(accuracy_scores.max())
print(accuracy_scores.min())
print(accuracy_scores > 0.85)
print(sum(accuracy_scores > 0.85))
print(sum(accuracy_scores))
