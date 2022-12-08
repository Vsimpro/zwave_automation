# Libraries
import time

# Modules
import modules.config

from modules.relay import *
from modules.bridge import *

# Testing out the modules.
def main():
    Zwave = Bridge()
    Zwave.login() # Log in

    # relay go click clack
    Zwave.getDevices()
    print("------------"*6)
    while 1:
        
        Zwave.relay_on(Zwave.devices[0])
        time.sleep(1)

        Zwave.relay_off(Zwave.devices[0])
        time.sleep(1)
    
if __name__ == "__main__":
    main()