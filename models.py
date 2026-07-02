from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# Todo veritabanı modeli
class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    is_completed = Column(Boolean, default=False) # Varsayılan: Tamamlanmadı
    deadline = Column(String, nullable=True) # Deadline alanı
