import os
from groq import Groq
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # ← updated model name!
    messages=[{"role": "user", "content": "Say hello in one sentence!"}],
)

print(response.choices[0].message.content)

models_df = {
    "model": ["Chat-GPT", "Gemini", "Claude", "Copilot", "Sora"],
    "accuracy": [0.87, 0.79, 0.99, 0.91, 0.56],
    "company": ["OpenAI", "Google", "Anthropic", "Microsoft", "OpenAI"],
    "parameters_billions": [1800, 540, 137, 350, 70],
}

df = pd.DataFrame(models_df)
best_index = df["accuracy"].idxmax()
best_model = df.loc[best_index, "model"]

summary = f"""

Here is a dataset of AI models:
{df}

Best model: {best_model}
Average accuracy: {df["accuracy"].mean()}
"""

print(summary)