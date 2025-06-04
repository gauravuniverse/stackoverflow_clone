import streamlit as st
import requests
import os

# API = "http://0.0.0.0:8000/api"
API = os.getenv("API_URL", "http://localhost:8000/api")


st.title("Stack Overflow Clone")

query = st.text_input("Enter your programming question:")
reranked = st.checkbox("Use LLM Reranked")
if query:
    res = requests.get(f"{API}/search/", params={"q": query, "rr": reranked}).json()
    st.subheader("Original StackOverflow Answers")
    print(f"res={res}")
    for ans in res["original"]:
        st.markdown(f"- **Score**: {ans['score']}")
        st.markdown(ans["body"], unsafe_allow_html=True)
        st.markdown(f"[Link]({ans['link']})")

    st.subheader("LLM Reranked Answers")
    if res["reranked"]:
        st.text(res["reranked"][0])

st.sidebar.title("Recent Searches")
recent = requests.get(f"{API}/recent/").json()
for q in recent:
    st.sidebar.write(q)
