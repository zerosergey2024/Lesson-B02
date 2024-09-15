import requests

def get_random_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and 'url' in data[0]:
            return data[0]['url']
    return None

import pytest
from unittest.mock import patch

# Создаем фейковый успешный ответ
def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('requests.get')
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{'url': 'https://example.com/cat.jpg'}]
    mock_get.return_value = mock_response

    cat_data = get_random_cat_image()
    assert cat_data == 'https://example.com/cat.jpg'

# Создаем фейковый неуспешный ответ (например, 404)
def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('requests.get')
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    assert get_random_cat_image() is None

# Запуск тестов с помощью pytest
if __name__ == '__main__':
    pytest.main()

