# Dockerfile
FROM python:3.11-slim

WORKDIR /app
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
