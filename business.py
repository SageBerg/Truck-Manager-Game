from queue import PriorityQueue
from datetime import timedelta
from random import choice

class Company(object):
    def __init__(self, world):
        self.name = 'Common Market Industrial Lines'
        self.money = 0
        self.truckers = dict()
        self.world = world

    def assign_job(self, job_id, trucker):
        job = trucker.place.jobs.pop(job_id)
        trucker.job = job
        job.trucker = trucker
        finish_time = self.get_soonest_completion_datetime(job)
        self.world.action_queue.put((finish_time, job))

    def get_shortest_path_km(self, job):
        pq = PriorityQueue()
        nodes = dict()
        starting_node = [0, job.start_place]
        nodes[job.start_place.name] = starting_node
        pq.put(starting_node)
        i = 100000
        for _, place in self.world.places.items():
            if place is not job.start_place:
                node = [i, place]
                nodes[place.name] = node
                pq.put(node)
            i += 1

        current_place = None
        while current_place is not job.finish_place:
            current_node = pq.get()
            current_distance = current_node[0]
            current_place = current_node[1]
            for _, route in current_place.routes.items():
                if route.distance + current_distance < nodes[route.destination.name][0]:
                    nodes[route.destination.name][0] = route.distance + current_distance
        return current_distance

    def get_soonest_completion_datetime(self, job):
        shortest_distance = self.get_shortest_path_km(job)
        soonest_completion_datetime = self.world.time + timedelta(minutes=shortest_distance)
        return soonest_completion_datetime

class Trucker(object):
    def __init__(self, name, place, company):
        self.name = name
        self.place = place
        self.job = None
        self.company = company

    def complete_job(self):
        self.place = self.job.finish_place
        self.company.money = self.job.value
        self.job = None

class Job(object):
    def __init__(self, cargo, value, start_place, finish_place):
        self.cargo = cargo
        self.value = value
        self.start_place = start_place
        self.finish_place = finish_place
        self.trucker = None

    def __gt__(self, other_job):
        return self.name > other_job.name

class JobMarket(object):
    cargos = [
        'Books',
        'Lumber',
        'Eggs',
        'Gasoline',
        'Musical Instruments',
        'Vaccines',
        'Paper',
    ]

    def __init__(self, world):
        self.world = world
        self.current_job_id = 0

    def get_job_id(self):
        self.current_job_id += 1
        return str(self.current_job_id)

    def add_job(self):
        start_place = self.world.places[choice(list(self.world.places.keys()))]
        finish_place = self.world.places[choice(list(self.world.places.keys()))]
        while start_place is finish_place:
            finish_place = self.world.places[choice(list(self.world.places.keys()))]
        cargo = choice(self.cargos)
        job = Job(cargo, 0, start_place, finish_place)
        pay = self.world.company.get_shortest_path_km(job) * choice([3, 4, 5, 6, 7])
        job.value = pay
        start_place.jobs[self.get_job_id()] = job
