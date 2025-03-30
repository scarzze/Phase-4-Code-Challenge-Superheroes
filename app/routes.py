from flask import Blueprint, jsonify, request
from .models import db, Hero, Power, HeroPower
from .serializers import HeroSchema, PowerSchema

# Use one blueprint to keep things simple
api_bp = Blueprint('api_bp', __name__)

# Schemas for converting our models to JSON
hero_schema = HeroSchema()             # single hero
heroes_schema = HeroSchema(many=True)    # list of heroes
power_schema = PowerSchema()           # single power
powers_schema = PowerSchema(many=True)  # list of powers

# ---------------------
# HEROES ENDPOINTS
# ---------------------

# GET /heroes: return a list of heroes (id, name, super_name)
@api_bp.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    # Only include the necessary fields
    result = [{'id': h.id, 'name': h.name, 'super_name': h.super_name} for h in heroes]
    return jsonify(result), 200

# GET /heroes/<id>: return hero details (with nested hero_powers) or error if not found
@api_bp.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero_schema.dump(hero)), 200

# ---------------------
# POWERS ENDPOINTS
# ---------------------

# GET /powers: return all powers
@api_bp.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify(powers_schema.dump(powers)), 200

# GET /powers/<id>: return a single power or error if not found
@api_bp.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power_schema.dump(power)), 200

# PATCH /powers/<id>: update a power's description
@api_bp.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    data = request.get_json()
    if 'description' not in data:
        return jsonify({"errors": ["Description is required"]}), 400
    power.description = data['description']
    try:
        power.validate_description()  # Custom method to validate description length
        db.session.commit()
    except ValueError as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400
    return jsonify(power_schema.dump(power)), 200

# ---------------------
# HERO POWERS ENDPOINT
# ---------------------

# POST /hero_powers: create a new HeroPower linking a hero and a power
@api_bp.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    # Check for required fields
    if not all(field in data for field in ['strength', 'hero_id', 'power_id']):
        return jsonify({"errors": ["Missing required fields"]}), 400
    hp = HeroPower(strength=data['strength'], hero_id=data['hero_id'], power_id=data['power_id'])
    try:
        hp.validate_strength()  # Custom method to check strength is valid
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
        "power": {
            "id": hp.power.id,
            "name": hp.power.name,
            "description": hp.power.description
        }
    }
    return jsonify(response), 201
