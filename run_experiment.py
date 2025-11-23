import os
import time
import pandas as pd
import openai
import anthropic
import requests

# Setup API keys as environment variables before running
openai.api_key = os.getenv("OPENAI_API_KEY")
claude_api_key = os.getenv("CLAUDE_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

def query_gpt4(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=512
    )
    return response['choices'][0]['message']['content'].strip()

def query_claude(prompt):
    client = anthropic.Client(claude_api_key)
    response = client.completions.create(
        model="claude-v1",
        prompt=prompt,
        max_tokens_to_sample=512,
        temperature=0.7,
        stop_sequences=["\n\n"]
    )
    return response.completion.strip()

def query_gemini(prompt):
    url = "https://api.gemini.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {gemini_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gemini-1.5-pro",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 512
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    return data['choices'][0]['message']['content'].strip()

def load_prompts():
    prompts = {}
    for fname in os.listdir("prompts"):
        if fname.endswith(".txt"):
            with open(os.path.join("prompts", fname), "r") as f:
                prompts[fname] = f.read()
    return prompts

def main():
    prompts = load_prompts()
    results = []
    llm_functions = {
        "gpt-4": query_gpt4,
        "claude": query_claude,
        "gemini": query_gemini
    }
    repetitions = 3
    for model, query_fn in llm_functions.items():
        for prompt_name, prompt_text in prompts.items():
            for rep in range(repetitions):
                try:
                    response = query_fn(prompt_text)
                except Exception as e:
                    response = f"Error: {e}"
                results.append({
                    "model": model,
                    "prompt_name": prompt_name,
                    "prompt": prompt_text,
                    "response": response,
                    "rep": rep,
                    "timestamp": time.time()
                })
                time.sleep(0.3)
    df = pd.DataFrame(results)
    os.makedirs("results", exist_ok=True)
    df.to_csv("results/raw_responses.csv", index=False)
    print("Experiment complete, results saved.")

if __name__ == "__main__":
    main()

#filepath modified for security