# 1. Start with a lightweight, official Python image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements file first
COPY requirements.txt .

# 4. Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code into the container
COPY . .

# 6. Expose the port the Flask app runs on
EXPOSE 5000

# 7. Define the command to start the app
CMD ["python3", "app.py"]
