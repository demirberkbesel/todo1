# tests/test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_list_todos():
    # Sadece text ekle
    response = client.post("/todos/", json={"text": "Test Todo"})
    assert response.status_code == 200
    
    response = client.get("/todos/")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) == 1
    assert todos[0]["text"] == "Test Todo"
    assert todos[0]["deadline"] is None

def test_create_todo_with_deadline():
    deadline = "2026-12-31"
    # Hem text hem deadline ekle
    response = client.post("/todos/", json={"text": "Deadline'lı görev", "deadline": deadline})
    assert response.status_code == 200
    
    response = client.get("/todos/")
    assert response.status_code == 200
    todos = response.json()
    # Artık izolasyon olduğu için her testte liste 1 elemanlı olacak
    assert len(todos) == 1
    assert todos[0]["deadline"] == deadline
