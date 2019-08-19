import bottle
from bottle import route, run, template

import paho.mqtt.client as mqtt
import sys

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
client.loop_stop() #stop the loop

# http routing

@bottle.get('/')
def index():
    return template('./templates/index.html')


@bottle.post('/say')
def say():
    text = bottle.request.POST['text']
    client.publish("trucdetest/jo/test",text) #publish


run(host='localhost', port=8080)
