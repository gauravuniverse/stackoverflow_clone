import requests

def fetch_so_answers(query: str):
    search_url = f"https://api.stackexchange.com/2.3/search/advanced"
    params = {
        "order": "desc", "sort": "relevance", "q": query,
        "site": "stackoverflow", "accepted": "True"
    }
    res = requests.get(search_url, params=params).json()
    answers = []
    for item in res.get("items", []):
        question_id = item["question_id"]
        ans_url = f"https://api.stackexchange.com/2.3/questions/{question_id}/answers"
        ans_params = {"order": "desc", "sort": "votes", "site": "stackoverflow", "filter": "withbody"}
        ans_res = requests.get(ans_url, params=ans_params).json()
        for ans in ans_res.get("items", []):
            answers.append({
                "answer_id": ans["answer_id"],
                "body": ans["body"],
                "score": ans["score"],
                "link": f"https://stackoverflow.com/a/{ans['answer_id']}"
            })
    return answers
