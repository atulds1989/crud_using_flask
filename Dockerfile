# Use the official Python image as the base image
FROM python:3.11.6

# Set the working directory in the container
WORKDIR /usr/src/myapp

# Copy the current directory contents into the container at /usr/src/myapp
COPY . /usr/src/myapp/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port number that Flask runs on
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python3", "app.py"]
