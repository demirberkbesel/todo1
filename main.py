from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Todo

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Veritabanı oturumu için bağımlılık
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ana sayfa (HTML'i yükle)
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

# Tüm todoları listele (API)
@app.get("/todos/")
def read_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

# Yeni todo oluştur (API)
@app.post("/todos/")
def create_todo(todo_data: dict, db: Session = Depends(get_db)):
    new_todo = Todo(text=todo_data["text"])
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Todo durumunu değiştir (Toggle) (API)
@app.put("/todos/{todo_id}/toggle")
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
