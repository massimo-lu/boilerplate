from fastapi.testclient import TestClient
from {{python_package_name}}.api.main import app

client = TestClient(app)


class TestAPI:
    def test_read_root(self):
        response = client.get("/")
        assert response.status_code == 200

    def test_read_hello(self):
        response = client.post("/hello", json={"name": "World"})
        assert response.status_code == 200
        assert "Hello" in response.text
