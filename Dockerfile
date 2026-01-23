FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir telethon

COPY start_work.py .

CMD ["python", "start_work.py"]
