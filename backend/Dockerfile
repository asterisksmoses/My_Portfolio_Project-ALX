# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies manually (e.g., Flask, pymysql, gunicorn)
RUN pip install flask pymysql gunicorn

# Expose port 5001 to the outside world
EXPOSE 5001

# Command to run the Gunicorn server on port 5001
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "backend:app:app"]