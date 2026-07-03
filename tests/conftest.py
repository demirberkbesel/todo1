import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database import Base, get_db
from main import app
from models import Todo  # Tablo tanımını Base'e yüklemek için import ediyoruz


# Testler için in-memory SQLite kullanıyoruz
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tabloları test veritabanında oluştur
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI bağımlılığını override et
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def setup_db():
    # Her testten önce tabloları sıfırla ve yeniden oluştur
    # Base'in tüm tabloları içerdiğinden emin olmak için database.py'den gelen Base kullanılıyor
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
