import pandas as pd

models_data = {
    "name": ["Chat-GPT", "Gemini", "Claude", "Copilot", "Sora"],
    "accuracy": [0.78, 0.81, 0.99, 0.92, 0.64],
    "company": ["OpenAI", "Google", "Anthropic", "Microsoft", "Google"],
    "version": [5, 1.8, 1.13523, 12, 3.3],
}

df = pd.DataFrame(models_data)
print(df.loc[df["accuracy"].idxmax()])

print(df["accuracy"].mean())


print(df.loc[df["company"] == "Google"])

df = df.sort_values("accuracy", ascending=False)

print(df)
