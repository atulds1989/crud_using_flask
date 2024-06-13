# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables for Flask
ENV FLASK_APP=app
ENV FLASK_ENV=development

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
