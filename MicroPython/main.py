from machine import Pin
import dht
import time
import json
from umqtt.simple import MQTTClient
from secrets import mqtt

def start_sensing():
    c = MQTTClient("humidity_sensor", mqtt["broker"])
    c.connect()

    sensor = dht.DHT11(Pin(27))

    while True:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        data = { "temperature": temp, "humidity": hum }
        data_str = json.dumps(data);

        print(data);
        
        c.publish("home/livingroom/sensor", data_str)
        
        time.sleep(30)

start_sensing()