models = ["Chat-GPT", "Gemini", "Copilot", "Claude"]
accuracy = [0.99, 0.6, 0.89, 1]

for i, model in enumerate(models):
    print(model, ": ", accuracy[i])
for i in range(5):
    print("Epoch:", i)
