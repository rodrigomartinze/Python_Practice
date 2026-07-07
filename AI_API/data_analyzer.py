import os
from groq import Groq
from dotenv import load_dotenv
import pandas as pd

load_dotenv()


models_df = {
    "model": ["Chat-GPT", "Gemini", "Claude", "Copilot", "Sora"],
    "accuracy": [0.87, 0.79, 0.99, 0.91, 0.56],
    "company": ["OpenAI", "Google", "Anthropic", "Microsoft", "OpenAI"],
    "parameters_billions": [1800, 540, 137, 350, 70],
}

models_df = pd.DataFrame(models_df)
text_df = models_df.to_string()
summary = f"Here is a dataset of AI models: \n {text_df} "
print(summary)
