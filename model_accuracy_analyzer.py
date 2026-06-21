import numpy as np

accuracy_scores = np.array([0.87, 0.98, 0.43, 0.67, 0.77, 0.89])
models_name = np.array(
    ["Chat-GPT", "Gemini", "Claude", "Copilot", "Blackbox", "GoogleIA"]
)

print(
    f"Mean: {accuracy_scores.mean()} Min: {accuracy_scores.min()} Max: {accuracy_scores.max()}"
)
print(sum(accuracy_scores > 0.80))

index = accuracy_scores.argmax()
print("The highest score is for: ", models_name[index])
