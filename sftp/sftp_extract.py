from dotenv import load_dotenv
import os
import paramiko

# Load environment variables from .env file
load_dotenv()

# SFTP connection details from .env
hostname = os.getenv("SFTP_HOST")
port = int(os.getenv("SFTP_PORT", 22))  # Default to port 22 if not set
username = os.getenv("SFTP_USERNAME")
password = os.getenv("SFTP_PASSWORD")

try:
    # Create an SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    ssh_client.connect(hostname, port, username, password)

    # Open an SFTP session
    sftp = ssh_client.open_sftp()

    # Example: List files in the remote directory
    remote_path = "/remote/directory/"
    print("Files in remote directory:")
    for file in sftp.listdir(remote_path):
        print(file)

    # Close the SFTP session
    sftp.close()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the SSH connection
    ssh_client.close()