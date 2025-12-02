# CertifyMe - Certificate Issuance Portal

A robust, Flask-based web application for issuing dynamic certificates to students. Built with a focus on clean architecture (MVC), security, and user experience.

## 🚀 Features

*   **Dynamic Certificate Generation**: Instantly generates a visual certificate with the student's name and course.
*   **Secure Form Handling**: Uses Flask-WTF for CSRF protection and input validation.
*   **Database Persistence**: Stores all issued certificates in a SQLite database using SQLAlchemy.
*   **Professional UI**: Styled with Bootstrap 5 for a responsive and modern look.
*   **Feedback System**: Interactive flash messages to confirm successful actions.

## 🛠️ Tech Stack

*   **Backend**: Python, Flask
*   **Database**: SQLite, SQLAlchemy, Flask-Migrate
*   **Frontend**: HTML5, Jinja2 Templates, Bootstrap 5
*   **Forms**: Flask-WTF

## ⚙️ Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Manish881-hub/CertifyME.git
    cd CertifyME
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, install manually: `pip install flask flask-sqlalchemy flask-migrate flask-wtf email-validator`)*

4.  **Initialize the Database**
    ```bash
    export FLASK_APP=microblog.py
    flask db upgrade
    ```

5.  **Run the Application**
    ```bash
    export FLASK_APP=microblog.py
    export FLASK_DEBUG=1  # Optional: for debug mode
    python -m flask run --port 5001
    ```

## 📖 Usage

1.  Open your browser and go to `http://127.0.0.1:5001/`.
2.  Enter the **Student Name** and **Course Name**.
3.  Click **Issue Certificate**.
4.  You will be redirected to a custom certificate page confirming completion.

## 📂 Project Structure

```
CertifyME/
├── app/
│   ├── templates/      # HTML files (base, index, certificate)
│   ├── __init__.py     # App factory & config
│   ├── forms.py        # Form definitions
│   ├── models.py       # Database models
│   └── routes.py       # View functions & logic
├── migrations/         # Database migration scripts
├── microblog.py        # Entry point
└── README.md           # This file
```
