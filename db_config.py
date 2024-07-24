import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def create_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dog_images (
        id SERIAL PRIMARY KEY,
        url TEXT NOT NULL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def save_image_url(url):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dog_images (url) VALUES (%s)", (url,))
    conn.commit()
    cursor.close()
    conn.close()
