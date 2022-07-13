import unittest
from app import app


class TestApp(unittest.TestCase):
    def create_app(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def send_url(self):
        with app.test_client() as self.client:
            return self.client.get('/?url=https://www.google.co.uk/', follow_redirects=True)

    def test_server(self):
        """Here we test the response works"""
        response = self.send_url()
        self.assertEqual(response.status_code, 200)

    def test_word(self):
        response = self.send_url()
        self.assertIn(b'google', response.data)


if __name__ == '__main__':
    unittest.main()
