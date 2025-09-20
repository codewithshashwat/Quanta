# Quanta – AI Chatbot (Django + Gemini API)

Quanta is an AI-powered chatbot built with **Django** and the **Google Gemini API**.  
It provides intelligent, context-aware responses with a clean web interface.

---

## 🚀 Features
- 🤖 Chatbot using **Gemini API**
- 🖥️ Django backend with REST endpoints
- 🎨 Responsive UI (HTML + CSS/JS)
- 🔐 Secure API key management
- 📦 Modular app structure (Django best practices)

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/quanta.git
cd quanta
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install django google-generativeai
```

### 4. Configure environment variables
Create a `api.txt` file in the project root:
```
your_api_key_here
```

### 5. Start the development server
```bash
python manage.py runserver
```

---

## 📖 Usage
- Start the Django server (`http://127.0.0.1:8000/`).
- Open the chatbot page.
- Enter your message → **Quanta** responds using Gemini API.

---

## 📂 Project Structure
```
Quanta/
│── App/             # Django app for chatbot
│   ├── views.py         # API + chatbot logic
│   ├── models.py        # Optional (if storing history)
│   ├── urls.py          # Routes
│   ├── templates/       # Frontend HTML
│   ├── static/          # CSS/JS
│
│── Project/              # Project settings
│   ├── settings.py
│   ├── urls.py
│
│── manage.py
│── requirements.txt
│── README.md
│── api.txt
```

---

## 🔧 Configuration
- Update **chatbot personality** or prompt settings in `views.py`.
- Customize UI in `templates/chatbot/`.
- Use `static/css/` for global styling.

---

## 🤝 Contributing
Pull requests are welcome!  
For major changes, please open an issue first to discuss.

---

## 📜 License
This project is licensed under the **MIT License**.
