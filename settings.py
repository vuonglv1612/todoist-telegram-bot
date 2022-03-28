from environs import Env

env = Env()
env.read_env()


class Config:
    TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")


config = Config()
