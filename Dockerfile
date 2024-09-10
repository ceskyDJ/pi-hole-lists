FROM python:3-slim

WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source codes
COPY src .

# Serve the web app
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-w 1", "app:app", "-b 0.0.0.0:5000"]
