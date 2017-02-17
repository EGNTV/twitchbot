import socket


class Connection:

    host = ""
    port = 80
    password = ""
    nickname = ""
    channel = ""

    def __init__(self,host,port,password,nickname,channel):
        self.sock = None
        self.host = host
        self.port = port
        self.password = password
        self.nickname = nickname
        self.channel = channel


    def connect(self):
        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))
        self.sock.send("PASS {}\r\n".format(self.password).encode("utf-8"))
        self.sock.send("USER {} 0 * :{}\r\n".format(self.nickname,self.nickname).encode("utf-8"))
        self.sock.send("NICK {}\r\n".format(self.nickname).encode("utf-8"))
        self.sock.send("JOIN {}\r\n".format(self.channel).encode("utf-8"))
        return self.sock

    def chat(self, msg):
        """
        Send a chat message to the server.
        Keyword arguments:
        sock -- the socket over which to send the message
        msg  -- the message to be sent
        """
        print("COMMAND: " + "PRIVMSG {} {}".format(self.channel, msg))
        bytes = self.sock.send("PRIVMSG {} {}\r\n".format(self.channel, msg).encode("utf-8"))
        print(bytes)

    def ban(self, user):
        """
        Ban a user from the current channel.
        Keyword arguments:
        sock -- the socket over which to send the ban command
        user -- the user to be banned
        """
        self.chat(self.sock, ".ban {}".format(user))

    def timeout(self,sock, user, secs=600):
        """
        Time out a user for a set period of time.
        Keyword arguments:
        sock -- the socket over which to send the timeout command
        user -- the user to be timed out
        secs -- the length of the timeout in seconds (default 600)
        """
        self.chat(self.sock, ".timeout {}".format(user, secs))