import requests

class Relay:
    def __init__(self, id, type="null", title="null", state="null", product="null", metrics="null"):
        self.id = id
        self.type = type
        self.name = title 
        self.title = title 
        self.state = state
        self.product = product
        self.metrics = metrics
        
        # TODO: Get this from a config.
        self.IP = "192.168.0.33:8083"

        self.on_url  = f"http://{self.IP}/ZAutomation/api/v1/devices/{id}/command/on"
        self.off_url = f"http://{self.IP}/ZAutomation/api/v1/devices/{id}/command/off"

    def getName(self):
        return self.title

    def getState(self):
        return self.state

    def turn_on(self, headers):
        response = requests.get(self.on_url, headers=headers)
        return response

    def turn_off(self, headers):
        response = requests.get(self.off_url, headers=headers)
        return response