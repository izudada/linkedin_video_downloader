# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define an environment variable to specify the Flask environment
ENV FLASK_APP=main.py

# Expose the port that Flask will run on
EXPOSE 5000

# Default to "production" mode if FLASK_ENV is not set
CMD ["sh", "-c", "if [ \"$FLASK_ENV\" = \"development\" ]; then flask run --host=0.0.0.0; else flask run --host=0.0.0.0 --port=5000; fi"]
