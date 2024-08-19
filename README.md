
# User CRUD Service

This project provides a simple CRUD (Create, Read, Update, Delete) service for managing users. User data is handled securely with hashed passwords using bcrypt.


## Project Structure
```
user_crud/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── services.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_services.py
│
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.7 or later
- `bcrypt` for password hashing
- unittest for testing (included in Python's standard library)

## Setup

### Clone the repository:
```
git clone https://github.com/yourusername/my_project.git
cd my_project
```

### Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install the required dependencies:
```
pip install -r requirements.txt
```

## Running the Project
Run the main script to see the CRUD operations in action:
```
python app/main.py
This script demonstrates the basic usage of the UserService class.
```

## Running the Tests
Run the tests using unittest:
```
python -m unittest discover -s tests
```

## Code Overview
- `app/models.py`: Defines the User class with password hashing and verification methods.
- `app/services.py`: Contains the UserService class for managing users, including CRUD operations and password security.
- `app/main.py`: Demonstrates how to use the UserService.
- `tests/test_services.py`: Contains tests for the UserService class.
