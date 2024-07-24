from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = FastAPI()

# Configuración de AWS S3
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

class ImageRequest(BaseModel):
    num_images: int

@app.post("/download-dog-images/")
async def download_dog_images(request: ImageRequest):
    try:
        # Llamada a la función Lambda
        lambda_client = boto3.client(
            'lambda',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )
        
        response = lambda_client.invoke(
            FunctionName='my_dog_images_function',
            InvocationType='RequestResponse',
            Payload=json.dumps({"num_images": request.num_images})
        )
        
        response_payload = json.load(response['Payload'])
        return response_payload

    except (NoCredentialsError, PartialCredentialsError):
        raise HTTPException(status_code=500, detail="AWS credentials not found or incomplete.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
