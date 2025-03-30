# seed.py
# This script seeds the database with initial data for heroes, powers, and hero-power relationships.
# To run this file, execute: python seed.py

from app import create_app
from app.models import db, Hero, Power, HeroPower

# Create the Flask app using our factory function
app = create_app()

def seed_data():
    # Use the application context to interact with the database
    with app.app_context():
        # -- Optional: Clear existing data --
        # Uncomment the following lines if you wish to drop all tables and start fresh:
        # db.drop_all()
        # db.create_all()

        # --------------------------
        # SEED HEROES
        # --------------------------
        heroes = [
            Hero(name="Kamala Khan", super_name="Ms. Marvel"),
            Hero(name="Doreen Green", super_name="Squirrel Girl"),
            Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
            Hero(name="Janet Van Dyne", super_name="The Wasp"),
            Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
            Hero(name="Carol Danvers", super_name="Captain Marvel"),
            Hero(name="Jean Grey", super_name="Dark Phoenix"),
            Hero(name="Ororo Munroe", super_name="Storm"),
            Hero(name="Kitty Pryde", super_name="Shadowcat"),
            Hero(name="Elektra Natchios", super_name="Elektra")
        ]
        # Add each hero to the session
        for hero in heroes:
            db.session.add(hero)

        # --------------------------
        # SEED POWERS
        # --------------------------
        powers = [
            Power(name="super strength", description="gives the wielder super-human strengths"),
            Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
            Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
            Power(name="elasticity", description="can stretch the human body to extreme lengths")
        ]
        # Add each power to the session
        for power in powers:
            db.session.add(power)

        # Commit heroes and powers so that IDs are generated
        db.session.commit()

        # --------------------------
        # SEED HERO_POWER RELATIONSHIP
        # --------------------------
        # Example: Link Kamala Khan (the first hero) with flight (the second power) with a "Strong" strength
        hero_power = HeroPower(
            strength="Strong", 
            hero_id=heroes[0].id, 
            power_id=powers[1].id
        )
        db.session.add(hero_power)

        # Commit the hero_power relationship
        db.session.commit()

        print("Seed data added successfully.")

if __name__ == '__main__':
    seed_data()
