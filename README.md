# 🧠 ToDo-List-Gemini

AI destekli, kullanıcı tabanlı bir ToDo uygulaması. Google Gemini entegrasyonu sayesinde, kullanıcıların girdiği basit açıklamalar otomatik olarak daha detaylı hale getirilir. FastAPI, SQLAlchemy ve LangChain kullanılarak geliştirilmiştir.

---

## 🚀 Özellikler

- 📝 Kullanıcı tabanlı ToDo listesi
- 🤖 Google Gemini AI ile açıklamaları detaylandırma
- 🔐 JWT tabanlı kullanıcı kimlik doğrulama
- 📄 Jinja2 ile HTML şablonlama
- 🛠️ Alembic ile veritabanı migration desteği
- 🔒 Şifreleme ve güvenlik: bcrypt

---

## ⚙️ Kurulum

### 1. Repo'yu klonla

```bash
git clone https://github.com/Yusuf-Ymn/ToDo-List-Gemini.git
cd ToDo-List-Gemini
```

### 2. Ortamı hazırla
Python 3.10+ önerilir.

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. .env dosyasını oluştur
Proje dizinine .env dosyasını oluştur ve içine Google AI Studio üzerinden aldığın API anahtarını ekle:

```ini
GOOGLE_API_KEY="your_google_gemini_api_key_here"
```

## Uygulamayı Çalıştır

```bash
uvicorn main:app --reload
```
Uygulama tarayıcıda otomatik olarak şu adrese yönlendirir:
```bash
http://localhost:8000/todo/todo-page
```
---

## 🖥️ Ekran Görüntüleri
- Giriş / Kayıt sayfası
![Ekran görüntüsü 2025-06-10 175818](https://github.com/user-attachments/assets/b4a4f085-2aec-4e4b-bd7a-1c1c03d8a707)
![Ekran görüntüsü 2025-06-10 175835](https://github.com/user-attachments/assets/f77b6272-c0e9-454f-8717-b42f3483d897)
- Yeni görev ekleme ekranı
![Ekran görüntüsü 2025-06-10 180009](https://github.com/user-attachments/assets/00e4e4b3-91b4-48df-ad06-c9eb18d66da0)
- Todo listesi
![Ekran görüntüsü 2025-06-10 180859](https://github.com/user-attachments/assets/16f6edf5-92bf-4cc5-bb80-15425fa100e5)
- Görev düzenleme ekranı
![Ekran görüntüsü 2025-06-10 180118](https://github.com/user-attachments/assets/77c200a5-87e5-4024-b73c-562117e26ed4)









