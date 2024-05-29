# Inventory Management System

This is a simple inventory management system written in Python using Flask and SQLAlchemy.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment and activate it.
4. Install the requirements:

    ```sh
    pip install -r requirements.txt
    ```

5. Set up the database:

    ```sh
    export FLASK_APP=run.py
    export FLASK_ENV=development
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. Run the application:

    ```sh
    python run.py
    ```

## Endpoints

- **Add Item**: `POST /items`
- **View Items**: `GET /items`
- **Update Item**: `PUT /items/<id>`
- **Delete Item**: `DELETE /items/<id>`

## Data Format

### Add/Update Item

```json
{
    "name": "Item Name",
    "quantity": 10,
    "price": 19.99
}
