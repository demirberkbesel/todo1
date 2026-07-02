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

def test_create_todo_with_deadline():
    deadline = "2026-12-31"
    # Yeni bir test senaryosu: deadline ile ekleme
    response = client.post("/todos/", json={"text": "Deadline'lı görev", "deadline": deadline})
    assert response.status_code == 200
    
    # Listeleme isteğinde deadline dönüyor mu?
    response = client.get("/todos/")
    assert response.status_code == 200
    # Deadline alanının döndüğünü kontrol et
    assert response.json()[1]["deadline"] == deadline
