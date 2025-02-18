# Use Python 3.10 or 3.11 since Mediapipe is compatible
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local project files into the container
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Default command to run when container starts
CMD ["bash"]
