FROM python:3.10-slim
WORKDIR /app
COPY alg.py .
CMD ["sh", "-c", "python3 alg.py && tail -f /dev/null"]
