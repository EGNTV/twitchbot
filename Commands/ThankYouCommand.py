
import abc
from .abstract.MessageCommand import MessageCommand
from .abstract.Command import Command
import cfg


class ThankYouCommand(MessageCommand):

    def isAllowed(self, username):
        return True

    def getMessage(self,username):
        return "Mon plaisir @{}! Veux-tu du gâteau? 🎂 ".format(username)