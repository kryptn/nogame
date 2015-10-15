from nogame import db

class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True)

    planets = db.relationship('Planet')
    moons = db.relationship('Moon')
    fleets = db.relationship('Fleet')

class Planet(db.Model):
    __tablename__ = 'planet'

    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(32))
    planet_size = db.Column(db.Integer)
    position_galaxy = db.Column(db.Integer)
    position_system = db.Column(db.Integer)
    position_slot = db.Column(db.Integer)
    moon = db.Column(db.Boolean, defualt=False)


    @property
    def planet_slots(self):
        return self.planet_size / 15

    @property
    def position(self):
        return (self.position_galaxy, self.position_system, self.position_slot)
    
class Moon(Planet):
    __tablename__ = 'moon'

    @property
    def planet_slots(self):
        return 1 + 0 #buildings modify slots on moons
    
class Fleet(db.Model):
    __tablename__ = 'fleet'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    speed_modifier = db.Column(db.Integer)
    #composition
    #origin
    #destination

    @property
    def speed(self):
        # return slowest ship * modifier
        pass

# Unsure how to represent so far

buildings = {} # name, cost (x y z scaling), prod (x y z)

research = {} # name, cost (x y z scaling), benefit

defences = {} # name, attack, defense, cost (x y z)

ships = {} # name, cost (x y z), attack, defense, bonuses / weaknesses, 
           # speed, fuel requirements, mission types, cargo

"""

       player------
        v   v     v
    planet moon   v
        v   v     v
        ---------fleet

"""