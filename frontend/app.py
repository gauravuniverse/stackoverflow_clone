import streamlit as st
import requests

API = "http://localhost:8000/api"

st.title("Stack Overflow Clone")

query = st.text_input("Enter your programming question:")
if query:
    res = requests.get(f"{API}/search/", params={"q": query}).json()
    st.subheader("Original StackOverflow Answers")
    for ans in res["original"]:
        st.markdown(f"- **Score**: {ans['score']}")
        st.markdown(ans["body"], unsafe_allow_html=True)
        st.markdown(f"[Link]({ans['link']})")

    st.subheader("LLM Reranked Answers")
    st.text(res["reranked"][0])

st.sidebar.title("Recent Searches")
recent = requests.get(f"{API}/recent/").json()
for q in recent:
    st.sidebar.write(q)
