import unittest

from app.app import app


class RegistrationPageTests(unittest.TestCase):
    def test_home_page_loads(self):
        response = app.test_client().get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hey! Register Here", response.data)


if __name__ == "__main__":
    unittest.main()
