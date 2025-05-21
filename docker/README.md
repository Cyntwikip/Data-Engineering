# Docker Basics and Creating a Basic Docker Container

Docker is a platform that allows you to build, share, and run applications in lightweight, portable containers. Containers package an application and its dependencies, ensuring it runs consistently across different environments.

Docker is highly relevant in data engineering because it simplifies the process of building, deploying, and managing data pipelines and applications. Here’s why:

1. **Consistency Across Environments**:
   - Docker ensures that your data engineering workflows run the same way in development, testing, and production environments.

2. **Simplified Deployment**:
   - With Docker, you can package your data pipelines and tools into containers, making them easy to deploy on any system.

3. **Isolation**:
   - Docker containers provide isolated environments, preventing dependency conflicts between different tools or projects.

4. **Scalability**:
   - Docker works seamlessly with orchestration tools like Kubernetes, enabling you to scale your data pipelines to handle large datasets.

5. **Reproducibility**:
   - Docker images act as snapshots of your application, ensuring that anyone can reproduce the same environment by running the image.

By using Docker, data engineers can streamline workflows, reduce setup time, and ensure portability and reliability of their applications.

---

## Prerequisites

Before you begin, ensure the following:
- Docker is installed on your system.
  - [Download Docker](https://www.docker.com/products/docker-desktop)
- Basic knowledge of the command line.

---

## Key Docker Concepts

1. **Image**:
   - A lightweight, standalone, and executable package that includes everything needed to run a piece of software (code, runtime, libraries, etc.).
   - Think of it as a blueprint for creating containers.

2. **Container**:
   - A running instance of a Docker image.
   - Containers are isolated environments where your application runs.

3. **Dockerfile**:
   - A text file that contains instructions to build a Docker image.

---

## Creating a Basic Docker Container

### Step 1: Create a `Dockerfile`

A `Dockerfile` is used to define the environment and steps to build your application. Below is an example `Dockerfile` for a Python application:

```dockerfile
# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory's contents into the container
COPY . /app

# Install any required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run the application
CMD ["python", "sftp_extract.py"]
```

### Step 2: Build the Docker Image

Run the following command in the terminal to build the Docker image:

```bash
docker build -t sftp-extract-app .
```

- `-t sftp-extract-app`: Tags the image with the name `sftp-extract-app`.
- `.`: Specifies the current directory as the build context.

### Step 3: Run the Docker Container

Run the container using the image you just built:

```bash
docker run --rm sftp-extract-app
```

- `--rm`: Automatically removes the container after it stops.
- `sftp-extract-app`: The name of the image to run.

### Step 4: Access the Container (Optional)

If you want to interact with the container, you can run it in interactive mode:

```bash
docker run -it sftp-extract-app /bin/bash
```

This will give you a shell inside the container.

---

## Example Directory Structure

Here’s an example of how your project directory might look:

```
project/
├── Dockerfile
├── requirements.txt
├── sftp_extract.py
└── .env
```

- **`Dockerfile`**: Defines the Docker image.
- **`requirements.txt`**: Lists Python dependencies (e.g., `paramiko`, `python-dotenv`).
- **`sftp_extract.py`**: Your Python script.
- **`.env`**: Contains environment variables for SFTP credentials.

---

## Common Docker Commands

1. **List Running Containers**:
   ```bash
   docker ps
   ```

2. **Stop a Running Container**:
   ```bash
   docker stop <container_id>
   ```

3. **List All Containers (Including Stopped)**:
   ```bash
   docker ps -a
   ```

4. **Remove a Container**:
   ```bash
   docker rm <container_id>
   ```

5. **Remove an Image**:
   ```bash
   docker rmi <image_name>
   ```

---

## Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

---
