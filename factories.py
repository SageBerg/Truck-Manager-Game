from world import *

def connect_places(places, place_one, place_two, distance_km):
    places[place_one.name].routes[place_two.name] = Route(place_two, distance_km)
    places[place_two.name].routes[place_one.name] = Route(place_one, distance_km)

def europe_factory():
    world = World()

    paris = Place('Paris')
    amiens = Place('Amiens')
    lille = Place('Lille')
    calais = Place('Calais')
    le_harve = Place('Le Harve')
    reims = Place('Reims')
    brussels = Place('Brussels')

    world.places['Paris'] = paris
    world.places['Amiens'] = amiens
    world.places['Lille'] = lille
    world.places['Calais'] = calais
    world.places['LeHarve'] = le_harve
    world.places['Reims'] = reims
    world.places['Brussels'] = brussels
    connect_places(world.places, paris, amiens, 144)
    connect_places(world.places, lille, amiens, 144)
    connect_places(world.places, reims, amiens, 178)
    connect_places(world.places, reims, lille, 206)
    connect_places(world.places, calais, amiens, 160)
    connect_places(world.places, lille, calais, 111)
    connect_places(world.places, paris, reims, 144)
    connect_places(world.places, paris, le_harve, 202)
    connect_places(world.places, le_harve, calais, 274)
    connect_places(world.places, le_harve, amiens, 180)
    connect_places(world.places, lille, brussels, 120)

    world.job_market.add_job()

    world.company.truckers['Io'] = Trucker('Io', world.places['Paris'], world.company)
    return world
