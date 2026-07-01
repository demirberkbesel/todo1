# Tasarım Dokümanı: To-Do Web Uygulaması

Bu doküman, sade bir To-Do web uygulamasının mimarisini ve geliştirme sürecini tanımlar.

## Amaç
Kullanıcıların todo öğelerini yönetebileceği (oluşturma, listeleme, durum güncelleme, silme) basit, öğrenilebilir ve test edilebilir bir uygulama oluşturmak.

## Özellikler
1.  **Oluştur:** Yeni bir todo öğesi ekle.
2.  **Listele:** Mevcut tüm todo öğelerini göster.
3.  **Toggle:** Bir öğeyi tamamlandı/tamamlanmadı olarak işaretle.
4.  **Sil:** Bir todo öğesini kaldır.

## Mimari
-   **Backend:** Python, FastAPI.
-   **Veritabanı:** SQLite (SQLAlchemy ORM ile).
-   **Frontend:** Düz HTML/JS (Bol yorumlu, basit yapı).

## Dosya Yapısı
```text
/
├── main.py          # FastAPI uygulaması
├── models.py        # Veritabanı modelleri
├── database.py      # Veritabanı bağlantısı
├── templates/
│   └── index.html   # Frontend
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   └── test_models.py
└── requirements.txt
```

## Test Stratejisi
-   **Unit Tests:** Veritabanı modeli doğrulama.
-   **Integration Tests:** API endpoint'lerinin (CRUD) uçtan uca doğrulanması (`pytest` + `httpx`).

## Onay
Tasarım onaylandıktan sonra uygulama kodlanacaktır.
