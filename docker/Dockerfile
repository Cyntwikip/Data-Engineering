# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory's contents into the container
COPY . /app

# Install required Python packages
# RUN pip install --no-cache-dir streamlit
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default Streamlit port
EXPOSE 8600

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8600", "--server.address=0.0.0.0"]