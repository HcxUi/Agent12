import requests
import subprocess

USE_MODE = "auto"  # Options: "online", "offline", "auto"

def ask_gpt(prompt):
    if USE_MODE == "online" or USE_MODE == "auto":
        try:
            url = "https://api.aayushgpt.tech/api"
            payload = {"prompt": prompt}
            res = requests.post(url, json=payload, timeout=20)
            if res.status_code == 200:
                return res.json().get("response", "")
            elif USE_MODE == "online":
                return "Online GPT server not responding."
        except:
            if USE_MODE == "online":
                return "Error: GPT server is down."

    if USE_MODE == "offline" or USE_MODE == "auto":
        try:
            result = subprocess.run(["ollama", "run", "gemma"], input=prompt.encode(), stdout=subprocess.PIPE, timeout=60)
            return result.stdout.decode().strip()
        except:
            return "Error: Ollama model not available or crashed."

    return "AI response not available."