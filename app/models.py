from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    super_name = db.Column(db.String(80), nullable=False)
    # Relationship to HeroPower with cascade delete
    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete-orphan")

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', backref='power', cascade="all, delete-orphan")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    # Custom validation: description must be present and at least 20 characters long
    def validate_description(self):
        if not self.description or len(self.description) < 20:
            raise ValueError("Description must be at least 20 characters long.")

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(20), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    def __init__(self, strength, hero_id, power_id):
        self.strength = strength
        self.hero_id = hero_id
        self.power_id = power_id

    # Validation: strength must be 'Strong', 'Weak', or 'Average'
    def validate_strength(self):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if self.strength not in valid_strengths:
            raise ValueError("Strength must be one of: 'Strong', 'Weak', or 'Average'.")
