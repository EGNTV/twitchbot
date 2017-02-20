
import abc

class Command(metaclass=abc.ABCMeta):
    PERMISSION_ADMIN = "admin"
    PERMISSION_MODERATOR = "moderators"
    PERMISSION_STAFF = "staff"
    PERMISSION_GLOBAL_MODERATOR = "global_mods"
    PERMISSION_VIEWER = "viewers"

    @abc.abstractmethod
    def isAllowed(self):
        """Decide if the user can execute de command"""