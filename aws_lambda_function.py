import requests
import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import threading

s3 = boto3.client('s3')

def download_image(image_number, bucket_name, image_urls):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = response.json()['message']
    image_data = requests.get(image_url).content
    image_name = f"image_{image_number}.jpg"
    
    try:
        s3.put_object(Bucket=bucket_name, Key=image_name, Body=image_data)
        image_urls.append(f"s3://{bucket_name}/{image_name}")
    except (NoCredentialsError, PartialCredentialsError):
        return "AWS credentials not found or incomplete."
    except Exception as e:
        return str(e)

def lambda_handler(event, context):
    num_images = event.get("num_images", 1)
    bucket_name = os.getenv('S3_BUCKET_NAME')
    threads = []
    image_urls = []

    for i in range(num_images):
        thread = threading.Thread(target=download_image, args=(i+1, bucket_name, image_urls))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return {
        "statusCode": 200,
        "body": image_urls
    }
