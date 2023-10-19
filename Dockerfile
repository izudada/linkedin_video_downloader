# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Define an environment variable to specify the Flask environment
ENV FLASK_APP=main.py
ENV FLASK_ENV=development

# Expose the port that Flask will run on
EXPOSE 5000

# Start your Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
