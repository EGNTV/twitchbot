
import abc
from .Command import Command


class MessageCommand(Command):
    @abc.abstractmethod
    def getMessage(self,username):
        """Return the message to be sent"""