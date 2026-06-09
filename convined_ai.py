models = [
    {"name": "Chat-GPT", "accuracy": 0.95, "version": 11},
    {"name": "Gemini", "accuracy": 0.89, "version": 3},
    {"name": "Claude", "accuracy": 1, "version": 5.5},
]


def evaluate_model(model):
    print(f"{model["name"]} :  {model["accuracy"]} :  {model["version"]}")


for model in models:
    evaluate_model(model)
