import pandas as pd

data = {
    "model": ["Chat-GPT", "Gemini", "Copilot", "Claude"],
    "accuracy": [0.78, 0.87, 0.91, 0.99],
    "company": ["Open-AI", "Google", "Microsoft", "Antrophic"],
}

df = pd.DataFrame(data)
print(df)
print(df["accuracy"])
print(df[df["accuracy"] > 0.90])
