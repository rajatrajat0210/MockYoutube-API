# 🎬 Mock YouTube RESTful API

This is a mock YouTube RESTful API built using **Flask**, **Flask-RESTful**, and **SQLAlchemy**. It supports full CRUD operations to manage a video database, with fields like `name`, `views`, and `likes`.

The API is designed for educational and testing purposes and can be interacted with using `test.py` (included) or tools like **Postman**.

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- SQLite
- Gunicorn (for deployment)
- Requests (for testing)

---

## 🚀 Features

- Add new videos using `PUT`
- View video details using `GET`
- Update existing videos using `PATCH`
- Delete videos using `DELETE`
- Error handling for duplicate IDs, missing entries, etc.

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/mock-youtube-api.git
cd mock-youtube-api
```

### 2. Install dependencies and Run 
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

```bash
pip install -r requirements.txt
python main.py
```
