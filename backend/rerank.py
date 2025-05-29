from llama_cpp import Llama
import html2text

llm = Llama(model_path="../models/mistral-7b-instruct.Q4_K_M.gguf", n_ctx=2048)

def rerank_answers(question, answers):
    converter = html2text.HTML2Text()
    text_answers = [
        f"{i+1}. Score: {a['score']}\n{converter.handle(a['body'])}"
        for i, a in enumerate(answers[:5])
    ]
    prompt = f"Question: {question}\n\nAnswers:\n" + "\n\n".join(text_answers)
    prompt += "\n\nRe-rank these answers from most to least relevant. Provide them in ranked order with reasoning if needed."

    response = llm(prompt, max_tokens=512, stop=["</s>"])
    return [response["choices"][0]["text"]]
