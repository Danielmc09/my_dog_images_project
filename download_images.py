import requests
import os
import threading
from db_config import save_image_url
from time import time

IMAGE_DIR = 'images'

if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def download_image(image_number):
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        image_url = response.json()['message']
        image_data = requests.get(image_url).content
        image_path = os.path.join(IMAGE_DIR, f'image_{image_number}.jpg')
        with open(image_path, 'wb') as image_file:
            image_file.write(image_data)
        save_image_url(image_url)
        print(f'Image {image_number} downloaded and saved as {image_path}')
    except Exception as e:
        print(f'Error downloading image {image_number}: {e}')

def main():
    start_time = time()
    threads = []

    for i in range(1, 51):
        thread = threading.Thread(target=download_image, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time()
    print(f'Total time taken: {end_time - start_time} seconds')

if __name__ == '__main__':
    main()
