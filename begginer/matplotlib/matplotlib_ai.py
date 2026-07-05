import matplotlib.pyplot as plt

models = ["Chat-GTP", "Gemini", "Claude", "Copilot", "BlackBox"]
acuraccy = [0.89, 0.78, 0.99, 0.91, 0.62]


plt.bar(models, acuraccy)
plt.title("AI-MODELS")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.show()
plt.ylim(0, 1)
plt.tight_layout()
