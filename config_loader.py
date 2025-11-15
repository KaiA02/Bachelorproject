import configparser

config = configparser.ConfigParser()
config.read('config.ini')

OPENAI_API_KEY = config["OPENAI"]["API_KEY"]
