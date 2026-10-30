
FROM python:3.12-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root application user
RUN addgroup --system app && adduser --system --ingroup app app

# Copy application files and assign ownership
COPY --chown=app:app app/ ./app/

# Run the application as the non-root user
USER app

EXPOSE 5000

CMD ["python", "app/app.py"]
