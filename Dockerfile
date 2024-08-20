# Use an official Python runtime as a parent image
FROM python:3.11

# Install necessary system dependencies for Playwright and Xvfb
RUN apt-get update && apt-get install -y \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libxkbcommon0 \
    libasound2 \
    libxshmfence1 \
    libglu1-mesa \
    xvfb \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and its dependencies
RUN python -m playwright install
RUN python -m playwright install-deps

# Run Playwright tests with Xvfb
# CMD ["xvfb-run", "pytest"]
# CMD ["sh", "-c", "echo 'Starting tests...' && ls -la && pytest -v"]
CMD ["xvfb-run", "-a", "pytest", "-v"]
