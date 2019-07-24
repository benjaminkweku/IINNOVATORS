
import paho.mqtt.client as mqtt
import time
import requests
from gpiozero import LED
led=LED(17)   

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")
Connected = False  # global variable for the state of the connection
client = mqtt.Client()
client.on_connect = on_connect
client.connect("104.248.163.70", 1883, 60)
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)
try:
    while True:
        
        message ="there is light"
        
        for i in message:
           while True:
                 message=input("input your message")
                 if message=="off light":
                      led.off()
                 elif message=="light on":
                      led.on()
                      client.publish("benjamin/mick","LikeMe:" + message)
                   
                      print("there is light")
                      continue
                 else:
                    led.on()
                    time.sleep(5)
                    led.off()
                    continue
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()