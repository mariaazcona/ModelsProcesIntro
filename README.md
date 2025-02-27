# Shopping List
Authors: Maria Azcona Garcia

## Requirements

- Python 3.x
- Django 3.x or higher
- pip (Python package manager)
- Virtualenv (optional)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mariaazcona/ModelsProcesIntro.git
cd ModelsProcesIntro
```

### 2. Create a virtual environment (optional)

On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

On Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Add example data
This project uses example product models sourced from the JSON file products.json. The dataset is extracted from the supermarket-web-example repository, originally available at: supermarket-web-example/products.json. To import these models:

```bash
python manage.py import_products
```

If you want to delete all products:
```bash
python manage.py delete_products
```

### 7. Run the server

```bash
python manage.py runserver
```

Server will be running on: http://127.0.0.1:8000/

### 8. Access the admin panel (optional)

You can access Django’s admin panel at: http://127.0.0.1:8000/admin/
