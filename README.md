# Book Management API

A Django REST Framework-based API for managing books and authors with JWT authentication.

## Features

- JWT Authentication
- User Registration and Login
- Author Management
- Book Management
- Permission-based Access Control
- Token Refresh Mechanism

## Requirements

- Python 3.x
- Django
- Django REST Framework
- Django REST Framework Simple JWT
- Django CORS Headers

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Book
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Apply migrations:
```bash
python manage.py migrate
```

4. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication

#### Register
- **URL**: `/register/`
- **Method**: `POST`
- **Data**:
```json
{
    "username": "your_username",
    "email": "your_email@example.com",
    "password": "your_password",
    "password2": "your_password"
}
```
- **Success Response**: Returns user data and JWT tokens

#### Login
- **URL**: `/login/`
- **Method**: `POST`
- **Data**:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
- **Success Response**: Returns JWT tokens

#### Refresh Token
- **URL**: `/token/refresh/`
- **Method**: `POST`
- **Data**:
```json
{
    "refresh": "your_refresh_token"
}
```
- **Success Response**: Returns new access token

### Authors

#### List/Create Authors
- **URL**: `/authors/`
- **Methods**: 
  - `GET` (public)
  - `POST` (authenticated)
- **POST Data**:
```json
{
    "name": "Author Name",
    "email": "author@example.com",
    "active": true
}
```

#### Get/Update/Delete Author
- **URL**: `/authors/<id>/`
- **Methods**: 
  - `GET` (authenticated)
  - `PUT` (owner/staff only)
  - `DELETE` (owner/staff only)
- **PUT Data**:
```json
{
    "name": "Updated Name",
    "email": "updated@example.com",
    "active": true
}
```

### Books

#### List/Create Books
- **URL**: `/books/`
- **Methods**: 
  - `GET` (public)
  - `POST` (authenticated)
- **POST Data**:
```json
{
    "title": "Book Title",
    "author": 1,
    "release_date": "2025-01-19",
    "pages": 200,
    "active": true
}
```

#### Get/Update/Delete Book
- **URL**: `/books/<id>/`
- **Methods**: 
  - `GET` (authenticated)
  - `PUT` (author's owner/staff only)
  - `DELETE` (author's owner/staff only)
- **PUT Data**:
```json
{
    "title": "Updated Title",
    "author": 1,
    "release_date": "2025-01-19",
    "pages": 250,
    "active": true
}
```

## Authentication

The API uses JWT (JSON Web Token) authentication. To access protected endpoints:

1. First obtain the access token through login or registration
2. Include the token in the Authorization header:
```
Authorization: Bearer <your_access_token>
```

## Permissions

- Public endpoints (no authentication required):
  - GET /authors/
  - GET /books/
  - POST /register/
  - POST /login/

- Authenticated endpoints:
  - All other endpoints require authentication
  - PUT/DELETE operations on authors and books are restricted to owners and staff members

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful GET/PUT requests
- 201: Successful POST requests
- 204: Successful DELETE requests
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found

## Models

### Author
- user (OneToOne with Django User)
- name (CharField)
- email (EmailField)
- active (BooleanField)

### Book
- title (CharField)
- author (ForeignKey to Author)
- release_date (DateField)
- pages (IntegerField)
- active (BooleanField)
