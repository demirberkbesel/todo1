# tests/e2e/test_todo_app.py
from playwright.sync_api import Page, expect

def test_add_todo_and_see_in_list(page: Page):
    """
    Playwright ile uçtan uca (E2E) test:
    1. Uygulama sayfasını açar.
    2. Yeni bir görev girer.
    3. 'Ekle' butonuna basar.
    4. Görevin listede göründüğünü doğrular.
    """
    
    # 1. Uygulama sayfasını aç
    page.goto("http://127.0.0.1:8000")
    
    # 2. Görev gir (index.html'deki 'todoInput' ID'li input'u kullanıyoruz)
    todo_text = "Playwright ile e2e testi"
    page.fill("#todoInput", todo_text)
    
    # 3. 'Ekle' butonuna bas (index.html'deki button)
    page.click("text=Ekle")
    
    # 4. Görevin listede göründüğünü kontrol et (ul içerisindeki li)
    # Listeyi buluyoruz ve içerik kontrolü yapıyoruz
    todo_item = page.locator("#todoList li")
    
    # Listenin boş olmadığını ve beklediğimiz metni içerdiğini doğrula
    expect(todo_item).to_have_count(1)
    expect(todo_item.first).to_contain_text(todo_text)
