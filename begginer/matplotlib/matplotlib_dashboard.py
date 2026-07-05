import matplotlib.pyplot as plt

models = ["Chat-GPT", "Gemini", "Claude", "Copilot", "BlackBox"]
accuracy = [0.89, 0.78, 0.99, 0.91, 0.62]

plt.figure()
plt.bar(models, accuracy)
plt.title("AI-MODELS")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.tight_layout()

plt.show()


epochs = [1, 2, 3, 4, 5, 6]
accuracy_progress = [0.60, 0.70, 0.78, 0.85, 0.91, 0.97]

plt.figure()
plt.plot(epochs, accuracy_progress)
plt.title("Training Progress")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.ylim(0, 1)

plt.tight_layout()

plt.show()
