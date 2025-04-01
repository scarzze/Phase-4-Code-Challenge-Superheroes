from . import db

# Allowed strength values for HeroPower
ALLOWED_STRENGTHS = ['Strong', 'Weak', 'Average']

class Hero(db.Model):
    __tablename__ = 'heroes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    super_name = db.Column(db.String(80), nullable=False)
    
    # Relationship: A Hero has many HeroPower records; cascade deletes
    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete-orphan")
    
    def to_dict(self):
        """Convert Hero instance to dictionary, including nested hero powers."""
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
            "hero_powers": [hp.to_dict() for hp in self.hero_powers]
        }

class Power(db.Model):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String, nullable=False)
    
    # Relationship: A Power has many HeroPower records; cascade deletes
    hero_powers = db.relationship('HeroPower', backref='power', cascade="all, delete-orphan")
    
    def validate_description(self):
        """Ensure description is at least 20 characters long."""
        if not self.description or len(self.description) < 20:
            raise ValueError("Description must be at least 20 characters long.")
    
    def to_dict(self):
        """Convert Power instance to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(20), nullable=False)
    
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    
    def validate_strength(self):
        """Ensure strength is one of the allowed values."""
        if self.strength not in ALLOWED_STRENGTHS:
            raise ValueError("Strength must be one of: 'Strong', 'Weak', 'Average'.")
    
    def to_dict(self):
        """Convert HeroPower instance to dictionary with nested power info."""
        return {
            "id": self.id,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
            "strength": self.strength,
            "power": self.power.to_dict() if self.power else None
        }
