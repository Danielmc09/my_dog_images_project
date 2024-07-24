
# My Dog Images Project

Este proyecto permite descargar imágenes aleatorias de perros utilizando AWS Lambda y almacenarlas en un bucket S3, a través de una API REST desarrollada con FastAPI. La descarga de imágenes se realiza de manera simultánea utilizando multithreading para mejorar la eficiencia.

## Requisitos

- Python 3.x
- AWS CLI configurado
- FastAPI
- Boto3
- Requests
- Pydantic
- Uvicorn
- Python-dotenv

## Instalación

1. Clona este repositorio.
2. Crea un entorno virtual y actívalo.
3. Instala las dependencias:

```sh
pip install -r requirements.txt
```

4. Configura tus credenciales de AWS y otros parámetros en un archivo `.env` en el directorio raíz del proyecto:

```env
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=your_aws_region
S3_BUCKET_NAME=your_s3_bucket_name
```

## Uso

Ejecuta la aplicación FastAPI:

```sh
uvicorn app.main:app --reload
```

Accede a la API en `http://localhost:8000` y utiliza el endpoint `/download-dog-images/` para solicitar un número de imágenes de perros.

### Ejemplo de uso:

```sh
curl -X POST "http://localhost:8000/download-dog-images/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"num_images": 5}'
```

Esto descargará 5 imágenes de perros y las guardará en tu bucket S3 configurado.

## Configuraciones en AWS

1. **Crear un bucket S3**: Ve a la consola de S3 y crea un nuevo bucket.
2. **Configurar AWS Lambda**:
    - Ve a la consola de Lambda y crea una nueva función llamada `my_dog_images_function`.
    - Selecciona "Author from scratch".
    - Configura un rol con permisos para acceder a S3.
3. **Agregar la lógica de Lambda**:
    - Copia el contenido de `aws_lambda_function.py` a la consola de Lambda.
    - Configura las variables de entorno en Lambda para las credenciales de AWS y el nombre del bucket.
4. **Configurar API Gateway** (opcional):
    - Si deseas exponer la función Lambda a través de un endpoint HTTP, puedes configurar un API Gateway.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.


Autor: <a href="https://www.linkedin.com/in/danielmendietadeveloper/">Angel Daniel Menideta Castillo</a> © 2024