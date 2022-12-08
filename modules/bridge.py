# Libraries
import json, requests

# Modules
from modules.relay import *
from modules.config import *
from modules.logger import  *


# Global Variables
MODULE_NAME = "BRIDGE"

class Bridge:
    def __init__(self):
        self.devices = []
        self.auth_cookie = ""
        
        # TODO: Get these from a config.
        self.IP = settings.bridge_address
        self.debug = True

        self.headers= {
            "accept":"application/json",
            "Content-Type":"application/json"
        }


    def getCookie(self):
        # This might be obsolete.
        return self.auth_cookie
        
    def setCookie(self, cookie):
        # This might be obsolete.
        debug_print(f"[{MODULE_NAME}] setting authentication cookie as '{cookie}'")
        self.auth_cookie = cookie 
        self.headers["Cookie"] = f"ZWAYSession={cookie}"
        return 0        

    def relay_on(self, relay):
        debug_print(f"[{MODULE_NAME}]  Turning on \t{relay.id} ")
        if relay.turn_on(self.headers).status_code == 200:
            return 0

        debug_print(f"[{MODULE_NAME}]  Something went wrong. ")
        return 1

    def relay_off(self, relay):
        debug_print(f"[{MODULE_NAME}]  Turning off \t{relay.id} ")
        if relay.turn_off(self.headers).status_code == 200:
            return 0

        debug_print(f"[{MODULE_NAME}]  Something went wrong. ")
        return 1

    def getDevices(self):
        devices_url = f"http://{self.IP}/ZAutomation/api/v1/devices"

        debug_print(f"[{MODULE_NAME}]  Attempting to fetch devices connected ..")
        response = requests.get(devices_url, headers=self.headers)
        data = response.json()

        if int(data["code"]) == 200:
            debug_print(f"[{MODULE_NAME}]  Devices found: ")

            for device in data["data"]["devices"]:
                if device["permanently_hidden"] == True:
                    continue

                if device["deviceType"] == "switchBinary":
                    debug_print(f"\t{device['metrics']['title']}")
                    new_device = Relay(
                        device["id"],
                        device["deviceType"],
                        device["metrics"]["title"],
                        device["metrics"]["level"],
                        device["product"],
                        device["metrics"])

                    self.devices.append(new_device)
            

    def login(self):
        login_url = f"http://{self.IP}/ZAutomation/api/v1/login"
        payload = {
            "form": "True",         # TODO:
            "login":    settings.username,        # GET THESE FROM CONFIG
            "password": settings.password, # GET THESE FROM CONFIG
            "keepme":"false",       
            "default_ui":"1"
        }
        
        # Login via API
        debug_print(f"[{MODULE_NAME}] Attempting to log in.. ")
        response = requests.post(login_url, data=json.dumps(payload), headers=self.headers)
        
        if response.status_code == 200:
            debug_print(f"[{MODULE_NAME}] Logged in.")
            self.setCookie(response.json()["data"]["sid"]) 
            return response

        debug_print(f"[{MODULE_NAME}] Failed to log in.")
        return response

