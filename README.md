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

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install dependencies and Run 
```bash
pip install -r requirements.txt
python main.py
```

## Postman Collection for API Testing

A Postman collection file `MockYouTubeAPI.postman_collection.json` is included for easy testing of the API.

### What is it?

- Predefined requests for all CRUD operations on videos.
- Import into Postman to quickly test API endpoints without coding.

### How to use?

1. Open Postman and click **Import**.
2. Select `MockYouTubeAPI.postman_collection.json`.
3. Update the API base URL if needed (default: `http://127.0.0.1:5000/`).
4. Run requests to test functionality.

This helps verify endpoints, experiment with data, and share tests with others easily.

