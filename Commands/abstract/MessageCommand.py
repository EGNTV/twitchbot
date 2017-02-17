
import abc


class MessageCommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getMessage(self):
        """Return the message to be sent"""