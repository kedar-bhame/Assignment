# 📘 Assignment – Django Distributed Insert Simulator

This project demonstrates **multi-app Django architecture** with:

✔ Separate apps: `users`, `products`, `orders`  
✔ REST API using Django REST Framework  
✔ Swagger API docs using `drf-yasg`  
✔ A custom management command for **threaded concurrent inserts**  
✔ Application-level validation (no DB-level constraints)  
✔ SQLite database  

---

# 📸 Screenshots


### 🖼️ Project Folder Structure
![folder-structure](https://github.com/kedar-bhame/Assignment/issues/3#issue-3688535246)

### 🖼️  API in Browser
![API](https://github.com/kedar-bhame/Assignment/issues/4#issue-3688543113)

### 🖼️ Swagger UI
![swagger-ui](https://github.com/kedar-bhame/Assignment/issues/1#issue-3688515305)

### 🖼️ Database
![Database](https://github.com/kedar-bhame/Assignment/issues/5#issue-3688550640)

### 🖼️ Simulator Running in Terminal
![terminal-simulator](https://github.com/kedar-bhame/Assignment/issues/2#issue-3688526579)

---

# 📂 Project Structure

```
assignment/
│ manage.py
│ requirements.txt
│ README.md
│ db.sqlite3
│
├── assignment/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
└── orders/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    └── management/
        └── commands/
            └── run_simulator.py
```

---

# 🚀 Features

## ✔ Three Independent Django Apps
Each app contains:
- Model
- Serializer
- API View
- URLs

## ✔ REST API Endpoints

| Method | URL          | Description        |
|--------|--------------|--------------------|
| GET    | `/users/`    | List all users     |
| POST   | `/users/`    | Create user        |
| GET    | `/products/` | List all products  |
| POST   | `/products/` | Create product     |
| GET    | `/orders/`   | List all orders    |
| POST   | `/orders/`   | Create order       |

---

## ✔ Swagger / OpenAPI Documentation

Visit Swagger UI:
```
http://127.0.0.1:8000/swagger/
```

---

## ✔ Custom Management Command — `run_simulator`

Simulates **concurrent inserts** using Python threads:
- 10 users
- 10 products
- 10 orders

Each insert is validated and logged.

Run the simulator:
```bash
python manage.py run_simulator
```

Example Output:
```
[USER][U-1] 1 SUCCESS
[PRODUCT][P-4] 4 SUCCESS
[ORDER][O-8] 8 FAILED: quantity must be > 0
...
=== SUMMARY ===
Users: 9
Products: 9
Orders: 7
Done.
```

---

# 🛠 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/kedar-bhame/Assignment.git
cd Assignment
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start Server
```bash
python manage.py runserver
```

Then visit:
```
http://127.0.0.1:8000/users/
http://127.0.0.1:8000/products/
http://127.0.0.1:8000/orders/
```

---

# 🧪 Running the Concurrent Insert Simulator

```bash
python manage.py run_simulator
```

It will:
- Validate user/product/order data
- Insert concurrently with threads
- Print success/failure logs
- Show final summary

---

# 📦 requirements.txt

```
Django==5.2.2
djangorestframework==3.15.2
drf-yasg==1.21.7
PyYAML==6.0.2
uritemplate==4.1.1
```

---

# 🗃 Viewing SQLite Database

You can open `db.sqlite3` using:
- VS Code **SQLite Viewer** extension
- **DB Browser for SQLite**
- Terminal:
```
sqlite3 db.sqlite3
.tables
```

---

# 🙌 Author

**Kedar Bhame**  
Python & Django Developer