# Base image: stable Debian variant
FROM python:3.12-bullseye

# Set working directory
WORKDIR /app

# Ensure apt uses HTTPS and install system deps
RUN sed -i 's|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Upgrade pip & install Python deps
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Django
EXPOSE 8000

# Run migrations automatically and start server
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
