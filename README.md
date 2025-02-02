# MLB Personalized AI Highlights

## Backend Setup

Welcome to the backend setup guide for the MLB Personalized AI Highlights project. Follow these steps to get your Django backend up and running.

### Prerequisites

Ensure you have the following installed:
- Python 3.10 or higher
- pip (Python package installer)
- virtualenv (optional but recommended)

### Step-by-Step Setup

1. **Clone the Repository**

   ```sh
   git clone https://github.com/externalPointerVaraible/mlb-personalized-ai-highlights.git
   cd mlb-personalized-ai-highlights/backend
   ```

2. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up the Environment Variable**

4. **Getting Started with Django-Rest_Framework**
    ```sh
    cd mlb
    python manage.py makemigrations
    python manage.py migrate
    ```
    ---

    *Set up the admin account*

    ```sh
    python manage.py createsuperuser
    ```
    ---
    *Getting started with the server*
    ```sh
    python manage.py runserver
    ```
