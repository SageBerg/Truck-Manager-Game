class CLI(object):
    def __init__(self, world):
        self.world = world

    def run_cli(self):
        self.run_command('?')
        while True:
            command = input('$ ')
            if command == 'q':
                break
            self.run_command(command)

    def run_command(self, command):
        if command == '?':
            print(
'''
a: <job_id> <trucker_name>: assign job to trucker
j: jobs list
l: truckers list
m: show your money
q: quit
r: run simulation until next choice
t: show time
'''
            )
        elif command == 'a':
            job_id = '1'
            trucker_name = 'Io'
            company = self.world.company
            trucker = company.truckers[trucker_name]
            company.assign_job(job_id, trucker)
            print(trucker.job.finish_place)
        elif command[0] == 'a' and len(command.split()) == 3:
            split_command = command.split()
            job_id = split_command[1]
            trucker_name = split_command[2]

            company = self.world.company
            trucker = company.truckers[trucker_name]
            company.assign_job(job_id, trucker)
        elif command == 'j':
            self.list_jobs()
        elif command == 'l':
            self.list_truckers()
        elif command == 'm':
            print('$' + str(self.world.company.money))
        elif command == 'r':
            self.world.next_action()
        elif command == 't':
            print(self.world.time)
        else:
            print('Invalid command entered.')

    def list_jobs(self):
        for place in self.world.places:
            for job_id, job in self.world.places[place].jobs.items():
                print(job_id + ': ' +
                      job.cargo + ', $' +
                      str(job.value) + ', ' +
                      job.start_place.name + ' to ' + job.finish_place.name
                )

    def list_truckers(self):
        for _, trucker in self.world.company.truckers.items():
            print('Truckers:')
            if trucker.job == None:
                print(trucker.name + ' is in ' + trucker.place.name)
            else:
                print(trucker.name + ' is trucking to ' + trucker.job.finish_place.name)
