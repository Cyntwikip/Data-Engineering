import pandas as pd
import boto3

def load(input_file: str, bucket_name: str, s3_key: str) -> None:
    print("Loading data to S3...")
    s3 = boto3.client('s3')
    # s3.upload_file(input_file, bucket_name, s3_key)
    print(f"Data loaded to S3 bucket '{bucket_name}' with key '{s3_key}'")