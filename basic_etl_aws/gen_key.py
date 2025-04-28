import boto3

def generate_presigned_url(bucket_name, object_key, expiration=3600):
    """
    Generate a pre-signed URL for an S3 object.

    :param bucket_name: Name of the S3 bucket.
    :param object_key: Key of the S3 object.
    :param expiration: Time in seconds for the URL to remain valid (default: 3600 seconds = 1 hour).
    :return: Pre-signed URL as a string.
    """
    s3_client = boto3.client('s3')
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_key},
            ExpiresIn=expiration
        )
        return url
    except Exception as e:
        print(f"Error generating pre-signed URL: {e}")
        return None

# Example usage
bucket_name = "your-bucket-name"
object_key = "credit_approval.csv"
expiration_time = 3600  # 1 hour

url = generate_presigned_url(bucket_name, object_key, expiration_time)
if url:
    print(f"Pre-signed URL: {url}")