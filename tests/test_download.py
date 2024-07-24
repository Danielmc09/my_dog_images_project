import unittest
from download_images import download_image

class TestDownloadImages(unittest.TestCase):
    def test_download_image(self):
        result = download_image(1)
        self.assertIsNone(result) 

if __name__ == '__main__':
    unittest.main()
