# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole project (app.py, Models/, etc.)
COPY . .

# Expose the port Hugging Face uses
EXPOSE 7860

# Run FastAPI with Uvicorn (pointing to app.py → app = FastAPI())
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
