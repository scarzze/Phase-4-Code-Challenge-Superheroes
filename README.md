# Superheroes API

## Overview
This is a Flask-based API for managing superheroes, their powers, and their abilities. The API allows users to perform CRUD operations on heroes, powers, and their relationships. 

## Features
- List all heroes with their names and superhero identities.
- Retrieve detailed information about a specific hero, including their powers.
- List all available superpowers.
- Retrieve details of a specific power.
- Update the description of a power.
- Assign powers to heroes with strength levels (Strong, Weak, or Average).

## Technologies Used
- Python
- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite (Database)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/scarzze/phase-4-code-challenge-superheroes.git
   cd phase-4-code-challenge-superheroes
   ```

2. Create and activate a virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```sh
   flask db upgrade
   ```

5. Run the application:
   ```sh
   flask run
   ```

## API Endpoints

### Heroes
- `GET /heroes` - Retrieve all heroes.
- `GET /heroes/<id>` - Retrieve a specific hero by ID.

### Powers
- `GET /powers` - Retrieve all powers.
- `GET /powers/<id>` - Retrieve a specific power by ID.
- `PATCH /powers/<id>` - Update a power's description.

### Hero Powers
- `POST /hero_powers` - Assign a power to a hero with a strength level.

## Project Structure
```
project_root/
│── app/
│   ├── __init__.py  # App factory & configuration
│   ├── models.py    # Database models
│   ├── routes.py    # API routes
│── migrations/      # Database migrations
│── .venv/           # Virtual environment (ignored)
│── requirements.txt # Dependencies
│── README.md        # Documentation
│── config.py        # Configuration settings (if any)
```

## Welcome Page
The home route (`/`) will display a simple welcome message to indicate that the API is running.

## Notes
- Ensure that no other program is using port `5000` before running the application.
- Use Postman or `curl` to test API endpoints.
- The database is SQLite but can be changed to PostgreSQL or MySQL as needed.

## Author
Built by Scar. 