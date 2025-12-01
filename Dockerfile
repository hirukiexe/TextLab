FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything from bot/ into /app
COPY bot/ ./

# Run the bot directly
CMD ["python3", "__main__.py"]
