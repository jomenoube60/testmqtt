
import paho.mqtt.client as mqtt
import sys

import time

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
broker_address="crava.ch"
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.on_message=on_message
client.username_pw_set("pifou", "plop")
client.connect(broker_address) #connect to broker
client.loop_start()    #start the loop
client.subscribe("trucdetest/jo/test")

while True:
    text = sys.stdin.read()
    client.publish("trucdetest/jo/test",text)#publish
time.sleep(4) # wait
client.loop_stop() #stop the loop
