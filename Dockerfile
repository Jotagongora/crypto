# Use the official Python image as a parent image
FROM python:3.10

# Actualiza los paquetes e instala Vim
RUN apt-get update && apt-get install -y vim

# Set environment variables for unattended installation of MySQL
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container
WORKDIR ./crypto_bot

VOLUME /crypto_bot

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port on which your Django application will run (e.g., 8000)
EXPOSE 8000

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
