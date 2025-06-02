## Stackoverflow Clone

### Prerequisite
- Python 3

### Setup
Install Python Packages
```
pip3 install -r requirements.txt
```
For local LLM, you need to download a quantized .gguf model (e.g., Mistral) from Hugging Face

Link - https://huggingface.co/TheBloke/openchat-3.5-0106-GGUF/resolve/main/openchat-3.5-0106.Q4_K_M.gguf

Copy .gguf file inside `models` folder. Example:
```
cp ~/Downloads/openchat-3.5-0106.Q4_K_M.gguf models/
```

### Start Backend Server
```
cd backend/
uvicorn main:app --reload
```

### Start Frontend Server
```
cd frontend/
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```
