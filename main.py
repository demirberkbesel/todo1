from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base, get_db
from models import Todo
from pydantic import BaseModel

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Şemalar
class TodoCreate(BaseModel):
    text: str
    deadline: str | None = None

class TodoResponse(BaseModel):
    id: int
    text: str
    is_completed: bool
    deadline: str | None = None

    class Config:
        from_attributes = True

# Veritabanı oturumu için bağımlılık tanımı main.py'den kaldırıldı, database.py'den import edildi.

# Ana sayfa (HTML'i yükle)
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

# Tüm todoları listele (API)
@app.get("/todos/", response_model=list[TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

# Yeni todo oluştur (API)
@app.post("/todos/", response_model=TodoResponse)
def create_todo(todo_data: TodoCreate, db: Session = Depends(get_db)):
    new_todo = Todo(
        text=todo_data.text,
        deadline=todo_data.deadline
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Todo durumunu değiştir (Toggle) (API)
@app.put("/todos/{todo_id}/toggle", response_model=TodoResponse)
def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.is_completed = not todo.is_completed
    db.commit()
    return todo

# Todo sil (API)
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted"}
