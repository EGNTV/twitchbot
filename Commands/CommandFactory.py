from .ScoreCommand import ScoreCommand

class CommandFactory:

    def __init__(self):
        pass

    def create(type):
        commands = {
            '!score': ScoreCommand(),
            '': None
        }
        return commands.get(type);
