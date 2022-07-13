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
            return self.client.get('/?url=https://www.nate.tech/', follow_redirects=True)

    def send_incorrect_url(self):
        with app.test_client() as self.client:
            return self.client.get('/?url=https://www.naet.tech/', follow_redirects=True)

    def send_no_url(self):
        with app.test_client() as self.client:
            return self.client.get('/', follow_redirects=True)

    def test_server(self):
        """Test the response works"""
        response = self.send_url()
        self.assertEqual(response.status_code, 200)

    def test_word(self):
        """Test the expected word and number are found"""
        response = self.send_url()
        self.assertIn(b'<td>creator:</td><td>1</td>', response.data)

    def test_url_error(self):
        """Test the Incorrect URL error is shown"""
        response = self.send_incorrect_url()
        self.assertIn(b'Incorrect URL', response.data)

    def test_http_error(self):
        """Test the HTTP error is shown"""
        response = self.send_no_url()
        self.assertIn(b'HTTP error', response.data)


if __name__ == '__main__':
    unittest.main()
