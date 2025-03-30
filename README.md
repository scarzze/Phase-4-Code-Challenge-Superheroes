# Phase-4-Code-Challenge-Superheroes
# Superheroes API
Welcome to the Superheroes API! This project is a simple Flask application built to track heroes and their superpowers. Whether you're a developer looking to learn about building RESTful APIs or a superhero fan who loves tech, this project has something for you.

# Project Overview
The Superheroes API allows you to:

List Heroes: Get a list of heroes with their basic details.

View Hero Details: See detailed information about a specific hero, including their superpowers.

List Powers: Get a list of all available superpowers.

View Power Details: See detailed information about a specific power.

Update Powers: Modify a power's description (with validation to ensure it's descriptive enough).

Create Hero Powers: Link heroes with their powers by creating hero_power relationships.

# How It Works
The API is built using Flask and follows RESTful principles:

# Models & Relationships:

A Hero has many Powers through HeroPower.

A Power has many Heroes through HeroPower.

The HeroPower model ties them together, and validations ensure data consistency.

# Routes:

Endpoints follow a simple, clear structure (e.g., GET /heroes, PATCH /powers/<id>, etc.).

Responses are formatted as JSON, with nested data where needed.

# Database:

Uses SQLite by default (configured in __init__.py), with migrations managed via Flask-Migrate.

Validation:

Custom validations ensure that superpower descriptions are at least 20 characters long and that hero power strengths are one of: 'Strong', 'Weak', or 'Average'.

# Getting Started
Prerequisites
Python 3.6+

pip

# Setup Instructions
Clone the repository:

bash
Copy code
git clone <https://github.com/scarzze/Phase-4-Code-Challenge-Superheroes>
cd <Phase-4-Code-Challenge-Superheroes>
Create a virtual environment and activate it:


bash
Copy code
pip install -r requirements.txt
(If you don't have a requirements.txt file, you'll need to install Flask, Flask-SQLAlchemy, Flask-Migrate, and Marshmallow manually.)

Initialize the database:

bash
Copy code
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed the database run it to add some initial data for testing.

# Running the Application
To start the application, simply run:

bash
Copy code
python run.py
The app will start in debug mode on http://127.0.0.1:5000.

Testing the API
You can test the API endpoints using Postman or your favorite API client. A Postman collection is included in the repository (named challenge-2-superheroes.postman_collection.json). Simply import the file into Postman to get started.

Project Structure
bash
Copy code
/project
   /app
       __init__.py       # App factory and configuration
       models.py         # SQLAlchemy models and relationships
       routes.py         # API endpoints (routes)
       serializers.py    # Marshmallow schemas for JSON serialization
   run.py                # Entry point to run the Flask app
   README.md             # This file!
Contributing
Since this is a private project for learning and assessment purposes, contributions aren't expected. However, feel free to experiment with the code and make improvements for your own learning!

License
This project is provided as-is for educational purposes.

