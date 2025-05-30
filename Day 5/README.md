# 📝 Flask To-Do List Application

A simple and clean web-based To-Do List application built with **Python** and **Flask**.  
Originally implemented with in-memory storage, it is now enhanced with **PostgreSQL** for persistent data management using **SQLAlchemy ORM**.

---

## 🚀 Features

- ✅ Add new tasks using a web form  
- ✏️ Edit existing tasks on a separate page  
- 🗑️ Delete tasks  
- 🧠 Data stored persistently in **PostgreSQL**  
- 📦 Environment variables managed via `.env` for secure configuration  
- 🔧 Clean project structure, ready for Docker deployment (future scope)

---

### Installation

1. Clone the repository
2. Create and activate a virtual environment:
        python -m venv venv
        venv\Scripts\activate
3. Install dependencies:
        pip install -r requirements.txt
4. Set up PostgreSQL
        DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/to_do_app
5. Run the Application
        python app.py

