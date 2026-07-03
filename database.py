from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite veritabanı dosyası
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"

# Veritabanı motoru oluşturma
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Oturum oluşturucu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Temel model sınıfı
Base = declarative_base()

# Veritabanı oturumu için bağımlılık
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
