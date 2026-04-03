FROM python:3.10-slim
WORKDIR /app
COPY stats.py .
CMD ["python3", "maze.py"]
