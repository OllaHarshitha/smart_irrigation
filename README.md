# smart_irrigation

Wireless sensor network makes the irrigation smarter and easier. The entire field is monitored continuously through the sensor network.Through Zigbee communication, the soil moisture levels are transferred from routers to the main coordinator.At the main controller, the temperature is monitored, based on the temperature,humidity and soil moisture content the motor can be controlled automatically.
It can be observed on web,we can visualise data on
https://node-red-sqmxh-2022-07-23.mybluemix.net/ui

The creditals of our device was provided from IBM IOT platform which are mentioned in the document named IBM.We are generating the temperature,humidity, and soil moisture(instead of hardware,IBM cloud is acting as sensor by generating random values which is being processed with help of random module in python) based on that graphs are shown ,then If we want to turn the motor on then by clicking on that we can see on the python interpreter where in real world it can be observed motor turned on and by giving the motor off command motor will be turned off.


