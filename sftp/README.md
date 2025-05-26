# SFTP 

SFTP (Secure File Transfer Protocol) is a secure method for transferring files between systems over a network. It is widely used in data engineering to move data between legacy systems, cloud storage, and modern data pipelines.

---

## Why SFTP is Important in Data Engineering

1. **Legacy System Integration**:
   - Many organizations still rely on legacy systems that use SFTP for data exchange. SFTP provides a reliable way to integrate these systems into modern data workflows.

2. **Secure File Transfers**:
   - SFTP encrypts both the data and the authentication process, ensuring secure file transfers over untrusted networks.

3. **Automating Data Pipelines**:
   - SFTP is often used to automate the ingestion of data files (e.g., CSV, JSON) into data lakes, warehouses, or ETL pipelines.

4. **Cross-Platform Compatibility**:
   - SFTP works across different operating systems and platforms, making it a versatile choice for data engineering workflows.

5. **Handling Sensitive Data**:
   - SFTP is commonly used in industries like finance and healthcare, where secure data transfer is critical.

---

## Tools for SFTP

There are several tools and methods for performing SFTP operations:

1. **Command-Line Tools**:
   - Most operating systems come with built-in SFTP clients that can be used directly from the terminal.
   - Example:
     ```bash
     sftp username@hostname
     ```
   - Common commands:
     - `ls`: List files in the remote directory.
     - `get <filename>`: Download a file from the remote server.
     - `put <filename>`: Upload a file to the remote server.

2. **Python Libraries**:
   - Python provides libraries like [paramiko](https://www.paramiko.org/) for automating SFTP operations programmatically.
   - Example:
     - Listing files, downloading, and uploading files using Python scripts.

3. **GUI Tools**:
   - Tools like FileZilla, WinSCP, and Cyberduck provide graphical interfaces for SFTP operations, making it easier for non-technical users.

4. **Cloud-Based Solutions**:
   - Many cloud providers (e.g., AWS, Azure) offer managed SFTP services that integrate with cloud storage.

5. **Workflow Orchestration Tools**:
   - Tools like Apache Airflow and Prefect can automate SFTP operations as part of larger data workflows.

---

## Example: Using SFTP in Python

This repository includes a Python script `sftp_extract.py` that demonstrates how to perform basic SFTP operations using the `paramiko` library.

### Features:
- List files in a remote directory.
- List both files and folders with detailed attributes.
- Read and print the contents of a specific file.

### Prerequisites:
1. Install the required Python libraries:
   ```bash
   pip install python-dotenv paramiko
   ```

2. Create a `.env` file to store your SFTP credentials:
   ```
   SFTP_HOST=your-sftp-host
   SFTP_PORT=22
   SFTP_USERNAME=your-username
   SFTP_PASSWORD=your-password
   ```

---

## How to Use the Script

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Data-Engineering.git
   cd Data-Engineering/sftp
   ```

2. **Set Up Environment Variables**:
   - Add your SFTP credentials to the `.env` file.

3. **Run the Script**:
   ```bash
   python sftp_extract.py
   ```

4. **Output**:
   - The script will list files in the remote directory and display the contents of a specified file.

---

## Example Terminal Commands for SFTP

If you prefer using the terminal for SFTP operations, here are some common commands:

1. **Connect to an SFTP Server**:
   ```bash
   sftp username@hostname
   ```

2. **List Files in a Directory**:
   ```bash
   ls
   ```

3. **Download a File**:
   ```bash
   get <remote_file_path>
   ```

4. **Upload a File**:
   ```bash
   put <local_file_path>
   ```

5. **Exit the SFTP Session**:
   ```bash
   exit
   ```

---

## Best Practices for SFTP in Data Engineering

1. **Automate Transfers**:
   - Use Python scripts or workflow orchestration tools to automate SFTP operations as part of your data pipelines.

2. **Secure Credentials**:
   - Store SFTP credentials securely using environment variables or secret management tools.

3. **Monitor Transfers**:
   - Implement logging and monitoring to track file transfers and detect failures.

4. **Validate Data**:
   - Verify the integrity of transferred files to ensure data consistency.

5. **Use Managed Services**:
   - Consider using managed SFTP services from cloud providers for better scalability and reliability.

---

## Additional Resources

- [Paramiko Documentation](http://docs.paramiko.org/)
- [SFTP Command-Line Guide](https://linuxize.com/post/how-to-use-sftp-command-to-transfer-files/)
- [FileZilla](https://filezilla-project.org/)
- [AWS Transfer Family (Managed SFTP)](https://aws.amazon.com/aws-transfer-family/)

---

By integrating SFTP into your data engineering workflows, you can securely and efficiently transfer data between systems, bridging the gap between legacy systems and modern data platforms.
