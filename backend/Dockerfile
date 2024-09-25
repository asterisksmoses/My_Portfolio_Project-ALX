# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app/backend

# Copy the current directory contents into the container
COPY . /app/backend

# Install the required dependencies
RUN pip install Flask gunicorn

# Expose port 5001 to the outside world
EXPOSE 5001

# Run gunicorn with 4 worker processes, binding to port 5001
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "app:app"]