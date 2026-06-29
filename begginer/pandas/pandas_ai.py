import pandas as pd

data = {
    "model": ["Chat-GPT", "Gemini", "Copilot", "Claude"],
    "accuracy": [0.78, 0.87, 0.91, 0.99],
    "company": ["Open-AI", "Google", "Microsoft", "Anthropic"],
}

df = pd.DataFrame(data)
print(df)
print(df["accuracy"])
print(
    df[df["accuracy"] > 0.90]
)  # This line show us just the lines in the DataFrame which their accuracy is bigger than 0.90
