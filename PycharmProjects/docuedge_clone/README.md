# DocuEdge Clone

A simplified document management system built using Django and Django REST Framework. This project is inspired by Deloitte's DocuEdge and demonstrates basic document storage, API handling, and modular design.

## Features

- Upload and manage documents via REST API
- Retrieve and view documents in JSON format
- Basic CRUD operations
- Clean and modular Django structure

## Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite (default)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/docuedge-clone.git
cd docuedge-clone
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv env
env\Scripts\activate   # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Endpoints

- `GET /documents/` – List all documents
- `POST /documents/` – Upload a new document
- `GET /documents/<id>/` – Retrieve a specific document
- `PUT /documents/<id>/` – Update a document
- `DELETE /documents/<id>/` – Delete a document

## Folder Structure

```
docuedge-clone/
├── core/
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── docuedge_clone/
│   └── settings.py
├── manage.py
├── README.md
└── requirements.txt
```

## Future Improvements

- User Authentication
- Document Preview
- Search & Filters
- Frontend (React or Templates)
- Docker Support & Deployment

## License

This project is for educational and demo purposes only.
```