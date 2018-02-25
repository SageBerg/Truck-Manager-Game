from datetime import datetime
from queue import PriorityQueue

from business import *

class World(object):
    def __init__(self):
        self.places = dict()
        self.company = Company(self)
        self.job_market = JobMarket(self)
        self.time = datetime.now()
        self.action_queue = PriorityQueue()

    def next_action(self):
        job = self.action_queue.get()
        self.time = job[0]
        job[1].trucker.complete_job()

class Place(object):
    def __init__(self, name):
        self.name = name
        self.routes = dict()
        self.jobs = dict()

    def __gt__(self, other_place):
        return self.name > other_place.name

class Route(object):
    def __init__(self, destination, distance):
        self.destination = destination
        self.distance = distance
