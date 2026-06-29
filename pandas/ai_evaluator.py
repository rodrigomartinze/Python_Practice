import pandas as pd
import numpy as np

models_data = {
    "name": ["Chat-GPT", "Gemini", "Claude", "Copilot", "Sora"],
    "accuracy": [0.78, 0.81, 0.99, 0.92, 0.64],
    "company": ["OpenAI", "Google", "Anthropic", "Microsoft", "Google"],
    "version": [5, 1.8, 1.13523, 12, 3.3],
}

df = pd.DataFrame(models_data)


def evaluate_all(df):
    print(df["accuracy"].max())
    print(df["accuracy"].mean())
    print(df.sort_values("accuracy", ascending=False))


accuracy_array = np.array(models_data["accuracy"])
print(accuracy_array.mean())
print(accuracy_array.max())
print(accuracy_array.min())

evaluate_all(df)
