# 1. Use a base image with Python preinstalled
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Install system dependencies (needed for pandas, matplotlib, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements.txt into the container
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of your project files
COPY . .

# 7. Default command to run when container starts
CMD ["pytest", "-v"]
