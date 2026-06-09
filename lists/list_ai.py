models = ["Chat-GPT", "Gemini", "Claude", "Blackbox"]
accuracy = [0.7, 0.21, 0.12, 0.8]

print(models[0], accuracy[0])
print(models[-1], accuracy[-1])

models.append("Copilot")

print(len(models))
