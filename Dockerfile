FROM python:3.11-slim

WORKDIR /app

# Make /app the python module root
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "bot"]
