import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_addition(client):
    # This acts like an invisible user typing 5 + 3 into your website
    response = client.post('/', data={'num1': '5', 'num2': '3', 'operation': 'add'})
    # It checks if the website replies with exactly 8.0
    assert b'Result: 8.0' in response.data
