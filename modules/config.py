import sys, json

from modules.logger import * 

class Settings:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.bridge_address = ""

    def no_credentials_error(self):
        debug_print("Credentials can't be blank in 'config.json' ")
        sys.exit()

    def create_config(self):
        with open("config.json", "w+") as file:
            file.write("""{
    "bridge_address" : "192.168.0.33:8083",

        "credentials" : {
        "username" : "",
        "password" : ""
        },
                
    "debug" : false
}
""")

        self.no_credentials_error()

settings = Settings()
try:
    with open("config.json", "r") as file:
        config = json.load(file)
        try:
            if (config["credentials"]["username"] == "") or (config["credentials"]["username"] == ""):
                raise KeyError

            settings.username = config["credentials"]["username"]
            settings.password = config["credentials"]["password"]

        except KeyError:
            settings.no_credentials_error()

        try:
            if config["bridge_address"] == "":
                raise KeyError

            settings.bridge_address = config["bridge_address"]
        except KeyError:
            debug_print("Invalid or blank bridge_adress in 'config.json' ")

except FileNotFoundError as e:
    settings.create_config()
