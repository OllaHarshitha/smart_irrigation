#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "5vofs2",
        "typeId": "NodeMCU",
        "deviceId":"mcu123"
    },
    "auth": {
        "token": "smartirrigation123"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if m=="motoron" :
        print("Motor is switched on")
    elif m=="motoroff":
        print("Motor is switched off")

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    moist=random.randint(10,90)
    myData={'temperature':temp, 'humidity':hum,'soil_moisture':moist}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
