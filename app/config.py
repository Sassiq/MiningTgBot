import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://tg_bot:123@localhost:5432/GoldMine"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


BOT_TOKEN = os.getenv("BOT_TOKEN", "1891373209:AAGTLW9Ryz0rFD--U-r7gfFQd2p2lZjFxb4")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://17e414ef8a31.ngrok.io")
TELEGRAM_URL = "https://api.telegram.org"



