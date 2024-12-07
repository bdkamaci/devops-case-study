import pytest
from app.src.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'environment' in data

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_config_route(client):
    response = client.get('/config')
    assert response.status_code == 200
    data = response.get_json()
    assert 'database_host' in data
    assert 'app_name' in data