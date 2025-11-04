# 💹 CryptoDashboard - A DeFi Portfolio Tracker

This is a full-stack web application built with Python and Django that allows users to track the value of their cryptocurrency holdings in real-time.

## Features

* **Secure User Authentication:** Full signup, login, and logout system.
* **Portfolio Management (CRUD):** Users can add, update, and delete coins from their personal portfolio.
* **Smart Updates:** Adding a coin you already own will update the amount instead of creating a duplicate entry.
* **Live API Integration:** Fetches real-time crypto prices from the CoinGecko API.
* **Polished UI/UX:** Built with Bootstrap 5 for a clean, responsive layout.
* **Light/Dark Mode:** A persistent light/dark mode toggle that remembers user preference.

## Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, Bootstrap 5, JavaScript
* **Database:** SQLite3 (for development)
* **Forms:** `django-crispy-forms`
* **API:** `requests` (for CoinGecko)
* **Environment:** `django-decouple` (for secret management)

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
    cd YOUR-REPO-NAME
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create your secret `.env` file:**
    * Create a file named `.env` in the root directory.
    * Add your Django `SECRET_KEY` and `DEBUG` status:
        ```ini
        SECRET_KEY='your-new-secret-key-here'
        DEBUG=True
        ```

5.  **Run the database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser to access the admin:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8.  Open your browser to `http://127.0.0.1:8000/`!
