# Apache Airflow Setup Guide

Apache Airflow is a platform to programmatically author, schedule, and monitor workflows. It is widely used for orchestrating complex workflows and managing data pipelines. This guide will help you set up Airflow with Celery Executor and configure authentication.

---

## Prerequisites

- Python 3.9 or higher installed on your system.
- `pip` (Python package manager) installed.

---

## Installation

Install Apache Airflow with the Celery Executor using the following command:

```bash
pip install "apache-airflow[celery]==3.0.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.9.txt"
```

---

## Configuration

Set the AIRFLOW_HOME Environment Variable
Before running Airflow, set the AIRFLOW_HOME environment variable to specify the directory where Airflow will store its configuration and data:

```ini
export AIRFLOW_HOME=~/airflow
```

You can run this line in your shell/terminal.

### Modify `airflow.cfg`

1. Update the `auth_manager` setting in your `airflow.cfg` file to use the FAB (Flask App Builder) authentication manager:
   ```ini
   auth_manager = airflow.providers.fab.auth_manager.fab_auth_manager.FabAuthManager
   ```
   **Note**: This configuration is a work in progress and may require additional setup.

2. Alternatively, for Simple Auth, you can enable all users as admins by adding the following line to `airflow.cfg`:
   ```ini
   simple_auth_manager_all_admins = True
   ```

3. Add the following dag_bundle_config_list configuration to include multiple DAG folders to `airflow.cfg`:
   ```ini
   dag_bundle_config_list = [
      {
      "name": "dags-folder",
      "classpath": "airflow.dag_processing.bundles.local.LocalDagBundle",
      "kwargs": {}
      },
      {
      "name": "data-engineering-dags-folder",
      "classpath": "airflow.dag_processing.bundles.local.LocalDagBundle",
      "kwargs": {
            "path": "<REPOSITORY>/Data-Engineering/"
      }
      }
   ]
   ```

   Replace <REPOSITORY> with the absolute path to your repository.

---

## User Management

### Create an Admin User

To create an admin user, run the following command:
```bash
airflow users create --role Admin --username admin --email admin@example.com --firstname Admin --lastname User --password admin
```

### Retrieve Simple Auth Passwords

If you are using Simple Auth, you can find the generated passwords in the following file:
```bash
less $AIRFLOW_HOME/simple_auth_manager_passwords.json.generated
```

---

## Running the Airflow Web UI

1. Start the Airflow standalone server:
   ```bash
   airflow standalone
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

3. Log in using the credentials you created (e.g., `username: admin`, `password: admin`).

---

## Notes

- If you encounter issues with authentication, ensure that the `auth_manager` setting in `airflow.cfg` matches your desired authentication method.
- For advanced setups, consider integrating Airflow with LDAP, OAuth, or other authentication providers.

---
