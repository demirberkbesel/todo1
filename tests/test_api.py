# tests/test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_list_todos():
    response = client.post("/todos/", json={"text": "Test Todo"})
    assert response.status_code == 200
    
    response = client.get("/todos/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["text"] == "Test Todo"
