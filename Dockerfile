FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project (bot/, core/, handlers/, etc.)
COPY . .

# Run the bot using package mode (because of __main__.py)
CMD ["python3", "-m", "bot"]
