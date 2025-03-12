import pytest
from app import app  

@pytest.fixture
def client():
    """Создание тестового клиента для приложения Flask."""
    app.testing = True
    return app.test_client()

def test_home(client):
    """Проверяем, что главная страница возвращает код 200 и ожидаемый текст."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello Flask" in response.data
