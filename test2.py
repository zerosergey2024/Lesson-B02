import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
         return response.json()

    else:
         return None


import unittest
from unittest.mock import patch
import requests


class TestCatAPI(unittest.TestCase):

    @patch('requests.get')
    def test_successful_request(self, mock_get):
       # Создаем фейковый успешный ответ
       mock_response = unittest.mock.Mock()
       mock_response.status_code = 200
       mock_response.json.return_value = [{'url': 'https://example.com/cat.jpg'}]
       mock_get.return_value = mock_response

       # Проверяем, что функция возвращает правильный URL
       self.assertEqual(get_random_cat_image(), 'https://example.com/cat.jpg')

    @patch('requests.get')
    def test_unsuccessful_request(self, mock_get):
        # Создаем фейковый неуспешный ответ (например, 404)
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Проверяем, что функция возвращает None при неуспешном запросе
        self.assertIsNone(get_random_cat_image())

    @patch('requests.get', side_effect=requests.exceptions.RequestException)
    def test_request_exception(self, mock_get):
        # Симулируем ошибку сети
        self.assertIsNone(get_random_cat_image())


if __name__ == '__main__':
    unittest.main()


# @patch('requests.get')
# @patch('requests.get', side_effect=requests.exceptions.RequestException)