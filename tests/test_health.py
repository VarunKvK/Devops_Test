from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "DevOps Health Check API is running"
    }

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "devops-health-api"
    }


def test_version_endpoint():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {
        "version": "1.0.0"
    }