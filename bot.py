# bot.py
import cfg
import re
import time
from Connection import Connection
from Commands.CommandFactory import CommandFactory
from Commands.abstract.MessageCommand import MessageCommand






con = Connection(cfg.HOST, cfg.PORT,cfg.PASS,cfg.NICK,cfg.CHAN)
s = con.connect()

CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

while True:
    response = s.recv(1024).decode("utf-8")
    print(response)
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0) # return the entire match
        message = CHAT_MSG.sub("", response).rstrip()
        command = CommandFactory.create(message)

        if(command and isinstance(command, MessageCommand)):
            con.chat(command.getMessage())

    time.sleep(1 / cfg.RATE)
