# -------- Stage 1: Builder --------
FROM python:3.10-slim AS builder

WORKDIR /app
COPY alg.py .

# Validate / compile Python code
RUN python3 -m py_compile alg.py


# -------- Stage 2: Runtime --------
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /app/alg.py .

CMD ["python3", "alg.py"]
