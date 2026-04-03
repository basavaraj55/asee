FROM python:3.10-slim
WORKDIR /app
COPY log.py .
CMD ["python3", "log.py"]
