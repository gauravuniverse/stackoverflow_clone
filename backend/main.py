from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from stack_api import fetch_so_answers
from rerank import rerank_answers
from db import cache_question, get_recent_questions

app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

@app.get("/api/search/")
def search_stackoverflow(q: str = Query(...)):
    cache_question(q)
    answers = fetch_so_answers(q)
    reranked = rerank_answers(q, answers)
    return {"original": answers, "reranked": reranked}

@app.get("/api/recent/")
def get_recent():
    return get_recent_questions()
