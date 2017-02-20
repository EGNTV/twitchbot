from .ScoreCommand import ScoreCommand
from .ThankYouCommand import ThankYouCommand
import cfg

class CommandFactory:

    def __init__(self):
        pass

    def create(type,username):
        commands = {
            '!score': ScoreCommand(),
            'Merci @{} !'.format(cfg.DISPLAY_NAME) : ThankYouCommand(),
            '': None
        }
        command = commands.get(type)
        if command is not None and command.isAllowed(username):
            return command
        else:
            return False