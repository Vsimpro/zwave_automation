# Zwave Control
### Home automation control centre using the RaZberry 2- Gateway.
Control the home appliances with a Rasbperry Pi through the ZWave RaZberry 2- Gateway.
The project aims to help users automate their home and co-ordinate the usage of appliances like heating according to the electricity prices.

> :warning: Project is in an early state of release. Breaking changes may be made to APIs/core structures as the project matures.

### Features:
    - Find relays in the network and turn them on/off [✔- ish]
    
#### TODO:

    - Webpanel to control the ZWave Devices [✗]
    - Read metrics off of censors like temperature [✗]
    - Automate relays to turn on/off according to electricity price [✗] 

#### How to run:
Git clone the folder to a Raspberry Pi with the ZWave RaZberry 2- GateWay installed and run:

```
python3.* main.py 
```

Project should work with Python 3.9 -> upward.
