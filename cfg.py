import os

# cfg.py
HOST = "irc.twitch.tv"              # the Twitch IRC server
PORT = 6667                         # always use port 6667!
NICK = "egn_glados"            # your Twitch username, lowercase
DISPLAY_NAME = "EGN_GLaDOS"
PASS = "oauth:wr3jzxz1v8g55hjoeh4hntqvw19ap3" # your Twitch OAuth token
GAME = "hearthstone"
CLIENT_ID = "omjsg2voqls26xkifmmdilg7dqqvlg"
CHAN = "#snappydue"                   # the channel you want to join
CHAN_NICK = "snappydue"
RATE = (20/30) # messages per second
APP_PATH = os.path.dirname(os.path.abspath(__file__))
MODS = []
STAFF = []
ADMINS = []
GLOBAL_MODS = []
VIEWERS = []
