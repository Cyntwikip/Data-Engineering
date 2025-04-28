import pandas as pd
import boto3
from io import StringIO

def extract(source_url: str, output_file: str) -> None:
    print("Extracting data from S3...")

    # Initialize S3 client
    s3 = boto3.client('s3')

    # # Parse bucket name and object key from the S3 URL
    # bucket_name = source_url.split('/')[2]
    # print(bucket_name)
    # object_key = '/'.join(source_url.split('/')[3:])

    bucket_name = 'dlsu-msds-aws-intro-1'
    object_key = 'credit_approval.csv'

    # Download the file content from S3
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    file_content = response['Body'].read().decode('utf-8')

    # Read the CSV content into a DataFrame
    columns = ['A' + str(i) for i in range(1, 17)]
    df = pd.read_csv(StringIO(file_content), names=columns)

    # Save the DataFrame to a local file
    df.to_csv(output_file, index=False)
    print(f"Data extracted and saved to {output_file}")