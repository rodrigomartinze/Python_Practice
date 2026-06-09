def evaluate_model(model, accuracy):
    print(f"Model:  {model} |  Accuracy:  {accuracy}")


model_name = ["Chat-GPT", "Gemini", "Copilot", "Claude"]
accuracy = [0.99, 0.6, 0.89, 1]

for i in range(0, 3):
    evaluate_model(model_name[i], accuracy[i])
