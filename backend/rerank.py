import html2text
import requests
import os
import json

TOGETHER_API_KEY = "your-together-ai-key"

def rerank_answers(question, answers):
    print("inside rerank_answers")
    converter = html2text.HTML2Text()
    text_answers = [
        f"{i+1}. Score: {a['score']}\n{converter.handle(a['body'])}"
        for i, a in enumerate(answers[:5])
    ]
    prompt = f"Question: {question}\n\nAnswers:\n" + "\n\n".join(text_answers)
    prompt += "\n\nRe-rank these answers from most to least relevant. Provide them in ranked order with reasoning if needed."

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }


    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages":
            [
                {"role": "user",
                 "content": prompt
                 }
            ], 
        "stream": False
    }
    payload = json.dumps(payload)
    print(f"payload: {payload}")

    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers=headers,
        data=payload
    )

    print(f"rerank response: {response}")
    if response.status_code == 200:
        result = response.json()
        print(f"result === {result}")
        return [result["choices"][0]["message"]["content"].strip()]
    else:
        return []
