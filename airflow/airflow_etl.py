from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
# from airflow.utils.dates import days_ago
from datetime import datetime
from dotenv import load_dotenv
import os, sys


def set_directory():
    """
    Set the directory to the location of this script.
    This is useful for ensuring that relative paths work correctly.
    """
    # Get the absolute path of the current file
    current_file_path = os.path.abspath(__file__)

    # etl_dir = os.path.join(os.path.dirname(current_file_path), '') # add subfolder if needed
    # etl_dir = os.path.abspath(etl_dir)

    # Get the directory of the current file
    etl_dir = os.path.dirname(current_file_path)

    sys.path.append(etl_dir)

    return etl_dir

ETL_DIR = set_directory()

# Import your ETL functions
from step1_extract import extract
from step2_transform import transform
from step3_load import load

# Load environment variables from .env file
load_dotenv()

SOURCE_URL = os.getenv("SOURCE_URL")
RAW_FILE = os.getenv("RAW_FILE")
PROCESSED_FILE = os.getenv("PROCESSED_FILE")
OUTPUT_FILE = os.getenv("OUTPUT_FILE")

RAW_FILE = os.path.join(ETL_DIR, RAW_FILE)
PROCESSED_FILE = os.path.join(ETL_DIR, PROCESSED_FILE)
OUTPUT_FILE = os.path.join(ETL_DIR, OUTPUT_FILE)


# Define Python functions for each ETL step
def extract_task():
    extract(SOURCE_URL, RAW_FILE)

def transform_task():
    transform(RAW_FILE, PROCESSED_FILE)

def load_task():
    load(PROCESSED_FILE, OUTPUT_FILE)

# Define the DAG
with DAG(
    'etl_dag',
    # start_date=datetime(2025, 6, 1),
    start_date=datetime(2025, 5, 1),
    # start_date=days_ago(1),
    schedule=None,
    catchup=False
) as dag:
    # Task 0: Ensure directories exist
    ensure_directories_op = BashOperator(
        task_id='ensure_directories_task',
        # bash_command='echo pwd && mkdir -p ./data/output ./data/raw ./data/processed'
        bash_command=f"echo pwd && mkdir -p {os.path.join(ETL_DIR,'data/output')} {os.path.join(ETL_DIR,'data/raw')} {os.path.join(ETL_DIR,'data/processed')}"
    )

    # Task 1: Initiate ETL Pipeline
    initiate_op = BashOperator(
        task_id='initiate_etl_task',
        bash_command='echo "Initiate ETL Pipeline"'
    )

    # Task 2: Extract
    extract_op = PythonOperator(
        task_id='extract_task',
        python_callable=extract_task
    )

    # Task 3: Transform
    transform_op = PythonOperator(
        task_id='transform_task',
        python_callable=transform_task
    )

    # Task 4: Load
    load_op = PythonOperator(
        task_id='load_task',
        python_callable=load_task
    )

    # Define task dependencies
    # ensure_directories_op >> initiate_op >> extract_op >> transform_op >> load_op
    ensure_directories_op >> extract_op
    initiate_op >> extract_op
    extract_op >> transform_op >> load_op

print("DAG defined successfully.")