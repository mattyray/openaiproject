# Dockerfile
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run the server
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "django_project.asgi:application"]
RUN python manage.py collectstatic --noinput
