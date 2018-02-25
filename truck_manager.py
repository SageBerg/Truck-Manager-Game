from factories import europe_factory
from business import *
from cli import CLI

print(
'''
 _____________________
|                     | |___
|    Truck Manager    | |  o|_
|_____________________|_|_____|
"(@)(@)          (@)(@)*****(@)
'''
)

world = europe_factory()
cli = CLI(world)
cli.run_cli()
