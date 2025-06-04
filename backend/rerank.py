# from llama_cpp import Llama
# import html2text

# llm = Llama(model_path="../models/openchat-3.5-0106.Q4_K_M.gguf", n_ctx=2048)

# def rerank_answers(question, answers):
#     converter = html2text.HTML2Text()
#     text_answers = [
#         f"{i+1}. Score: {a['score']}\n{converter.handle(a['body'])}"
#         for i, a in enumerate(answers[:5])
#     ]
#     prompt = f"Question: {question}\n\nAnswers:\n" + "\n\n".join(text_answers)
#     prompt += "\n\nRe-rank these answers from most to least relevant. Provide them in ranked order with reasoning if needed."

#     response = llm(prompt, max_tokens=512, stop=["</s>"])
#     return [response["choices"][0]["text"]]

from openai import OpenAI
import html2text

client = OpenAI(api_key="your-openai-key")


def get_response(prompt):
    response = client.chat.completions.create(model="gpt-4.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=500)
    return response.choices[0].message.content

def rerank_answers(question, answers):
    converter = html2text.HTML2Text()
    text_answers = [
        f"{i+1}. Score: {a['score']}\n{converter.handle(a['body'])}"
        for i, a in enumerate(answers[:5])
    ]
    prompt = f"Question: {question}\n\nAnswers:\n" + "\n\n".join(text_answers)
    prompt += "\n\nRe-rank these answers from most to least relevant. Provide them in ranked order with reasoning if needed."

    response = get_response(prompt)
    print(response)
    return response
