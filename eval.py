import openai
import json

openai.api_key = "sk-..."  # Replace with your OpenAI key

def evaluate_response(prompt, response, expected_tone):
    system_prompt = (
        "You are an AI evaluator. Assess the following response for:
"
        "- Factual Accuracy (0–10)
"
        "- Coherence (0–10)
"
        "- Tone Alignment (0–10, does it match expected tone)
"
    )
    user_input = f"Prompt: {prompt}\n\nResponse: {response}\n\nExpected tone: {expected_tone}"

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    return completion["choices"][0]["message"]["content"]

if __name__ == "__main__":
    with open("samples.json") as f:
        samples = json.load(f)

    for i, sample in enumerate(samples):
        result = evaluate_response(sample["prompt"], sample["response"], sample["expected_tone"])
        print(f"\n--- Sample {i+1} ---\n{result}")