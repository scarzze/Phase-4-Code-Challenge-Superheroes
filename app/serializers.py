from marshmallow import Schema, fields, validates, ValidationError

class PowerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)

    @validates('description')
    def validate_description(self, value):
        if len(value) < 20:
            raise ValidationError("Description must be at least 20 characters long.")

class HeroPowerSchema(Schema):
    id = fields.Int(dump_only=True)
    strength = fields.Str(required=True)
    hero_id = fields.Int(required=True)
    power_id = fields.Int(required=True)
    # Include nested power data
    power = fields.Nested(PowerSchema, only=('id', 'name', 'description'))

class HeroSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    super_name = fields.Str(required=True)
    # Nest hero_powers to include details in GET /heroes/:id
    hero_powers = fields.Nested(HeroPowerSchema, many=True)
