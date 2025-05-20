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

# Constants for remote path and file to read
# REMOTE_PATH = "/home/sftpuser/"
# FILE_TO_READ = "/home/sftpuser/data/credit_approval_raw.csv"

# starts at user directory
REMOTE_PATH = "/"
FILE_TO_READ = "/data/credit_approval_raw.csv"

def list_files(sftp, remote_path):
    """List files in the remote directory."""
    print("Files in remote directory:")
    for file in sftp.listdir(remote_path):
        print(file)

def list_files_and_folders(sftp, remote_path):
    """List files and folders in the remote directory."""
    print(f"Contents of remote directory: {remote_path}")
    try:
        for item in sftp.listdir_attr(remote_path):
            if paramiko.S_ISDIR(item.st_mode):  # Check if it's a directory
                print(f"[DIR]  {item.filename}")
            else:
                print(f"[FILE] {item.filename}")
    except FileNotFoundError:
        print(f"Remote path {remote_path} not found.")

def read_file(sftp, file_path):
    """Read and print the contents of a specific file."""
    try:
        with sftp.file(file_path, "r") as remote_file:
            print(f"\nContents of {file_path}:")
            print(remote_file.read().decode("utf-8"))  # Decode bytes to string
    except FileNotFoundError:
        print(f"File {file_path} not found.")

def main():
    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        ssh_client.connect(hostname, port, username, password)

        # Open an SFTP session
        sftp = ssh_client.open_sftp()

        # Call modular functions
        list_files(sftp, REMOTE_PATH)
        # list_files_and_folders(sftp, REMOTE_PATH)
        read_file(sftp, FILE_TO_READ)

        # Close the SFTP session
        sftp.close()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the SSH connection
        ssh_client.close()

if __name__ == "__main__":
    main()