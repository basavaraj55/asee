FROM python:3.10-slim
WORKDIR /app
COPY alg.py .
CMD ["python3", "alg.py"]
