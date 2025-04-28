from step1_extract import extract
from step2_transform import transform
from step3_load import load
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SOURCE_URL = os.getenv("SOURCE_URL")
RAW_FILE = os.getenv("RAW_FILE")
PROCESSED_FILE = os.getenv("PROCESSED_FILE")
OUTPUT_FILE = os.getenv("OUTPUT_FILE")

def main():
    # Extract raw data
    extract(SOURCE_URL, RAW_FILE)
    
    # Transform raw data into processed data
    transform(RAW_FILE, PROCESSED_FILE)
    
    # Load processed data to S3
    load(PROCESSED_FILE, OUTPUT_FILE)

if __name__ == "__main__":
    main()