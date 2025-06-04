## Stackoverflow Clone

### Prerequisite
- Python 3
- Docker

### Setup

Update rerank.py line number 21 with the openai api key
```
rerank.py#21 client = OpenAI(api_key="your-openai-key")
```

#### Using Docker

Build the App using Docker
```
docker compose build
```

Start the App using Docker
```
docker compose up
```

#### Using command line
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

Start Backend Server
```
cd backend/
uvicorn main:app --reload
```

Start Frontend Server
```
cd frontend/
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```
