FROM python:3.13-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

COPY . .
ENV PATH=/root/.local/bin:$PATH

# config.ini must be provided at runtime (secret mount / env)
CMD ["python", "-m", "src.main"]
