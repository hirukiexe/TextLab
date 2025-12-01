FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for cache efficiency
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy remaining project files
COPY . .

CMD ["python3", "bot"]