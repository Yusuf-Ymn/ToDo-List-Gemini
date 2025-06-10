# 🧠 ToDo-List-Gemini

An AI-powered, user-based ToDo application. With Google Gemini integration, simple task descriptions entered by users are automatically enhanced into more detailed versions. Built using FastAPI, SQLAlchemy, and LangChain.

---

## 🚀 Features

- 📝 User-specific ToDo list
- 🤖 Automatic description enhancement using Google Gemini AI
- 🔐 JWT-based user authentication
- 📄 HTML templating with Jinja2
- 🛠️ Database migrations with Alembic
- 🔒 Password security with bcrypt

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Yusuf-Ymn/ToDo-List-Gemini.git
cd ToDo-List-Gemini
```

2. Set up the environment
Python 3.10+ is recommended.

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a .env file
Create a .env file in the project root and insert your API key from Google AI Studio:

```ini
GOOGLE_API_KEY="your_google_gemini_api_key_here"
```

## Run the Application

```bash
uvicorn main:app --reload
```
Once the server is running, you will be redirected to:
```bash
http://localhost:8000/todo/todo-page
```
---

## 🖥️ Screenshots
Login / Register Pages
![Ekran görüntüsü 2025-06-10 175818](https://github.com/user-attachments/assets/b4a4f085-2aec-4e4b-bd7a-1c1c03d8a707)
![Ekran görüntüsü 2025-06-10 175835](https://github.com/user-attachments/assets/f77b6272-c0e9-454f-8717-b42f3483d897)
- Add New Task Page
![Ekran görüntüsü 2025-06-10 180009](https://github.com/user-attachments/assets/00e4e4b3-91b4-48df-ad06-c9eb18d66da0)
- Todo list
![Ekran görüntüsü 2025-06-10 180859](https://github.com/user-attachments/assets/16f6edf5-92bf-4cc5-bb80-15425fa100e5)
- Edit Task Page
![Ekran görüntüsü 2025-06-10 180118](https://github.com/user-attachments/assets/77c200a5-87e5-4024-b73c-562117e26ed4)









