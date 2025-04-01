from flask import Blueprint, request, jsonify
from .models import db, Hero, Power, HeroPower

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/')
def home():
    print("Home route is working!")
    return "Welcome to the Superheroes API!"


# GET /heroes - List all heroes (basic info)
@api_bp.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    # Return a list of heroes with only id, name, and super_name
    result = [{"id": h.id, "name": h.name, "super_name": h.super_name} for h in heroes]
    return jsonify(result), 200

# GET /heroes/<id> - Return detailed hero info with nested hero powers
@api_bp.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict()), 200

# GET /powers - List all powers
@api_bp.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    result = [p.to_dict() for p in powers]
    return jsonify(result), 200

# GET /powers/<id> - Return specific power details
@api_bp.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

# PATCH /powers/<id> - Update power description
@api_bp.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    if "description" not in data:
        return jsonify({"errors": ["Description is required"]}), 400

    power.description = data["description"]
    try:
        power.validate_description()
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

    return jsonify(power.to_dict()), 200

# POST /hero_powers - Create a new HeroPower relationship
@api_bp.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    required_fields = ["strength", "hero_id", "power_id"]
    if not all(field in data for field in required_fields):
        return jsonify({"errors": ["Missing required fields"]}), 400

    hp = HeroPower(
        strength=data["strength"],
        hero_id=data["hero_id"],
        power_id=data["power_id"]
    )
    try:
        hp.validate_strength()
        db.session.add(hp)
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

    # Build response with nested hero and power info
    response = {
        "id": hp.id,
        "hero_id": hp.hero_id,
        "power_id": hp.power_id,
        "strength": hp.strength,
        "hero": {
            "id": hp.hero.id,
            "name": hp.hero.name,
            "super_name": hp.hero.super_name
        },
        "power": hp.power.to_dict()
    }
    return jsonify(response), 201
