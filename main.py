from download_images import main
from db_config import create_table
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

if __name__ == '__main__':
    create_table()
    main()
