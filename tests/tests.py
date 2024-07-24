import unittest
from db_config import create_connection, create_table, save_image_url

class TestDatabase(unittest.TestCase):
    def test_create_connection(self):
        conn = create_connection()
        self.assertIsNotNone(conn)
        conn.close()

    def test_create_table(self):
        create_table()
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dog_images")
        result = cursor.fetchall()
        self.assertIsNotNone(result)
        cursor.close()
        conn.close()

    def test_save_image_url(self):
        save_image_url('https://example.com/image.jpg')
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dog_images WHERE url = 'https://example.com/image.jpg'")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        cursor.close()
        conn.close()

if __name__ == '__main__':
    unittest.main()
