FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy complete project
COPY . .

# Run package (because entrypoint is bot/__main__.py)
CMD ["python3", "-m", "bot"]
