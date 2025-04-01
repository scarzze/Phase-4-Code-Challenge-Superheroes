from app import create_app
from app.models import db, Hero, Power,HeroPower

app = create_app()

with app.app_context():
    # (Optional) Drop and recreate tables for a clean slate
    db.drop_all()
    db.create_all()

    # Seed Powers
    power1 = Power(name="super strength", description="gives the wielder super-human strengths")
    power2 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
    power3 = Power(name="super human senses", description="allows the wielder to use her senses at a super-human level")
    power4 = Power(name="elasticity", description="can stretch the human body to extreme lengths")
    
    db.session.add_all([power1, power2, power3, power4])
    db.session.commit()

    # Seed Heroes
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    hero3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    hero4 = Hero(name="Janet Van Dyne", super_name="The Wasp")
    hero5 = Hero(name="Wanda Maximoff", super_name="Scarlet Witch")
    hero6 = Hero(name="Carol Danvers", super_name="Captain Marvel")
    hero7 = Hero(name="Jean Grey", super_name="Dark Phoenix")
    hero8 = Hero(name="Ororo Munroe", super_name="Storm")
    hero9 = Hero(name="Kitty Pryde", super_name="Shadowcat")
    hero10 = Hero(name="Elektra Natchios", super_name="Elektra")
    
    db.session.add_all([hero1, hero2, hero3, hero4, hero5, hero6, hero7, hero8, hero9, hero10])
    db.session.commit()

    # Seed HeroPower relationships
    hp1 = HeroPower(hero_id=hero1.id, power_id=power2.id, strength="Strong")
    # Add more HeroPower records as needed for testing...
    
    db.session.add(hp1)
    db.session.commit()

    print("Database seeded successfully with heroes and powers!")
