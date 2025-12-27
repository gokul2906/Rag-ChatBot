from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_db():
    r = client.get("/health/db")
    assert r.status_code == 200
    assert r.json()["ok"] is True
