import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
sudo = os.environ.get("SUDO", "")
HEROKU = os.environ.get("HEROKU", "APP-NAME")
APP_URL = "https://"+ HEROKU +".herokuapp.com/" + BOT_TOKEN
