FROM python:3.10-slim
WORKDIR /app
COPY . .
# RUN apt-get update && apt-get install -y python3-pip
RUN pip install fastapi uvicorn requests openai html2text
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
